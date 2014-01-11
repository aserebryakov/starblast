import pygame
import random
from pygame.locals import *
from Engine import *


class Enemy(ScreenObject):

    def __init__(self):
        self.BOXCORRECTION = 20
        self.ANIMATION_FPS = 10
        self.NORMAL_ANIMATION_CYCLIC = True
        self.normal_state_frames = ['graphics/enemy/asteroid.png']

        self.normal_animation = Animation(self.normal_state_frames, \
                                          self.ANIMATION_FPS,       \
                                          self.NORMAL_ANIMATION_CYCLIC)

        rand = random.Random()
        self.posy  = 0
        self.posx  = 0
        ScreenObject.__init__(self, self.normal_animation,\
                                    self.posx, self.posy)
        self.dx    = 0
        self.dy    = 0

    def update(self, *args):
        self.posx -= self.dx
        self.posy -= self.dy
        ScreenObject.update(self)

        if self.posx < 0:
            self.kill()

