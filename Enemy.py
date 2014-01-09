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

    def update(self, surface):
        self.posx -= 20
        ScreenObject.update(self, surface)

        if self.posx < 0:
            self.kill()

