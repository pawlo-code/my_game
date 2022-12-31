import pygame

class Pistol():
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect

        self.image = pygame.image.load('images/pistol.bmp')
        self.rect = self.image.get_rect()

        self.rect.midleft = self.screen_rect.midleft
        self.rect.y = self.screen_rect.centery
        self.rect.x += 50

        self.pistol_up = False
        self.pistol_down = False


    def update(self):
        if self.pistol_up and self.rect.top > self.screen_rect.top:
            self.rect.y -=1
        if self.pistol_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y +=1

    def blitme(self):
        self.screen.blit(self.image, self.rect)
