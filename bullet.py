import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen_rect

        self.rect = pygame.Rect(0,0, 15, 3)
        self.color = pygame.Color(180, 180, 180)
        self.rect.midleft = ai_game.pistol.rect.topright

    def update(self):
        self.rect.x += 1
        
        if self.rect.x > self.screen_rect.width:
            Sprite.kill(self)
            

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)