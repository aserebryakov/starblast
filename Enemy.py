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

