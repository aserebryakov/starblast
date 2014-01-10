import pygame
import random
from pygame.locals import *
from GameSettings import GameSettings
from ScreenObject import ScreenObject
from Animation import Animation


class Enemy(ScreenObject):

    def __init__(self):
        self.normal_state_frames = ['asteroid.png']
        self.normal_animation = Animation(self.normal_state_frames)

        rand = random.Random()
        self.posy = rand.uniform(0, GameSettings.SCREENHEIGHT)
        self.posx = GameSettings.SCREENWIDTH
        ScreenObject.__init__(self, self.normal_animation,\
                                    self.posx, self.posy)
        self.dx   = rand.uniform(10, 30)
        self.dy   = rand.uniform(-10, 10)

    def update(self, surface):
        self.posx -= self.dx
        self.posy -= self.dy
        ScreenObject.update(self, surface)

        if self.posx < 0:
            self.kill()

