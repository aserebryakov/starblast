import pygame
from pygame.locals import *
from GameSettings import GameSettings
from ScreenObject import ScreenObject

class Player(ScreenObject):
    BOXCORRECTION = 15

    def __init__(self):
        ScreenObject.__init__(self, 'ship.png')
        self.posx = 50
        self.posy = GameSettings.SCREENHEIGHT / 2

    def update(self, surface):
        key = pygame.key.get_pressed()

        if key[K_DOWN]:
            self.posy += 10
        elif key[K_UP]:
            self.posy -= 10
        elif key[K_RIGHT]:
            self.posx += 10
        elif key[K_LEFT]:
            self.posx -= 10

        self.rect.x = self.posx
        self.rect.y = self.posy + self.BOXCORRECTION
        surface.blit(self.image, (self.posx, self.posy))

