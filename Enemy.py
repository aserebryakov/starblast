import pygame
import random
from pygame.locals import *
from GameSettings import GameSettings
from ScreenObject import ScreenObject

class Enemy(ScreenObject):

    def __init__(self):
        ScreenObject.__init__(self, 'asteroid.png')
        rand = random.Random()
        self.posy = rand.uniform(0, GameSettings.SCREENHEIGHT)
        self.posx = GameSettings.SCREENWIDTH
        self.dx   = rand.uniform(10, 30)
        self.dy   = rand.uniform(-10, 10)

    def update(self, surface):
        self.posx -= self.dx
        self.posy -= self.dy
        ScreenObject.update(self, surface)

        if self.posx < 0:
            self.kill()

