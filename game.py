import sys

import pygame

from pistol import Pistol
from bullet import Bullet
from monster import Monster

class Game:
    def __init__(self):

        pygame.init()
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        self.screen_rect = self.screen.get_rect()

        self.points = 0
        self.live_points = 3

        self.pistol = Pistol(self)
        self.bullets = pygame.sprite.Group()
        self.monsters = pygame.sprite.Group()
        self.time = pygame.time
        self.tick = 0

    def _create_monster(self):
        check_tick = self.time.get_ticks()

        if (len(self.monsters) < 5 and (check_tick - self.tick) >= 1500):
            new_monster = Monster(self)
            self.monsters.add(new_monster)
            if not new_monster.random_position():
                self.monsters.remove(new_monster)
            self.tick = self.time.get_ticks()

    def _update_monsters(self):
        self._create_monster()
        self.monsters.update()
        for monster in self.monsters:
            if monster.rect.x < 0:
                self.monsters.remove(monster)
        if pygame.sprite.groupcollide(self.monsters, self.bullets, True, True):
            self.points += 1
        if pygame.sprite.spritecollide(self.pistol, self.monsters, True):
            self.live_points -= 1
            

    def _create_bullet(self):
        if len(self.bullets) < 5:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _bullets_update(self):
        self.bullets.update()

    def run_game(self):
        while True:
            
            self._update_events()

            if self.live_points > 0:
                self._update_monsters()
                self._bullets_update()
                self._update_screen()

            pygame.display.flip()

    def _update_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._update_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._update_keyup_events(event)

    def _update_keydown_events(self, event):
        if event.key == pygame.K_DOWN:
            self.pistol.pistol_down = True
        if event.key == pygame.K_UP:
            self.pistol.pistol_up = True
        if event.key == pygame.K_SPACE:
            self._create_bullet()

    def _update_keyup_events(self, event):
        if event.key == pygame.K_DOWN:
            self.pistol.pistol_down = False
        if event.key == pygame.K_UP:
            self.pistol.pistol_up = False

    def _update_screen(self):
        self.screen.fill((0,0,0))
        self.pistol.blitme()
        self.pistol.update()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        self.monsters.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run_game()