import pygame
from pygame.locals import *
from GameSettings import GameSettings
from ScreenObject import ScreenObject

class Player(ScreenObject):
    BOXCORRECTION = 20

    def __init__(self):
        ScreenObject.__init__(self, 'ship.png')
        self.posx = 50
        self.posy = GameSettings.SCREENHEIGHT / 2
        self.dx   = 10
        self.dy   = 10

    def update(self, surface):
        key = pygame.key.get_pressed()

        if key[K_DOWN]:
            self.posy += self.dy 
        elif key[K_UP]:
            self.posy -= self.dy
        elif key[K_RIGHT]:
            self.posx += self.dx
        elif key[K_LEFT]:
            self.posx -= self.dx

        self.rect.x = self.posx
        self.rect.y = self.posy + self.BOXCORRECTION/2
        surface.blit(self.image, (self.posx, self.posy))

