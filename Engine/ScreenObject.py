import pygame
from pygame.locals import *
from Animation import Animation

class ScreenObject(pygame.sprite.Sprite):

    def __init__(self, anim, posx, posy):
        self.posx = posx
        self.posy = posy
        self.dx   = 0
        self.dy   = 0
        pygame.sprite.Sprite.__init__(self)
        self.animation = anim
        self.image  = self.animation.get_frame()
        self.rect   = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy

    def update(self, *arg):
        self.image  = self.animation.get_frame()
        self.rect   = self.image.get_rect()
        self.rect.x = self.posx
        self.rect.y = self.posy

