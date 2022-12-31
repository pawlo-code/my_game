from random import randint

import pygame
from pygame.sprite import Sprite

class Monster(Sprite):
    def __init__(self, ai_game):
        super().__init__()

        self.ai_game = ai_game
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect

        self.image = pygame.image.load('images/monster.png')
        self.rect = self.image.get_rect()
    
    def update(self):
        self.x -= 0.5
        self.rect.x = self.x

    def random_position(self):
        self.half_monster_h = self.rect.height / 2
        self.half_monster_w = self.rect.width / 2

        random_y = randint(
                   self.half_monster_h,
                   (self.screen_rect.height - self.half_monster_h)
        )
        random_x = randint(
                   (int(self.screen_rect.right * 0.7)),
                   (self.screen_rect.right - self.half_monster_w)

        )

        for monster in self.ai_game.monsters:
            if monster.rect.colliderect((random_x, random_y, 100, 100)):
                return False

        self.rect.centerx = random_x
        self.rect.centery = random_y
        self.x = float(self.rect.x)
        return True