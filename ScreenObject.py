import pygame
from pygame.locals import *

class ScreenObject(pygame.sprite.Sprite):
    posx = 0
    posy = 0
    rect = pygame.Rect(10, 10, 10, 10)

    def __init__(self, imagePath):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(imagePath)
        self.rect = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy

    def update(self, surface):
        self.rect.x = self.posx
        self.rect.y = self.posy
        surface.blit(self.image, (self.posx, self.posy))
