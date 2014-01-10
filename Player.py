import pygame
from pygame.locals import *
from Engine import *

class Player(ScreenObject):

    def __init__(self):
        self.BOXCORRECTION = 20
        self.ANIMATION_FPS = 3
        self.NORMAL_ANIMATION_CYCLIC = True
        self.radius = 10
        self.normal_state_frames = ['graphics/player/ship_01.png',\
                                    'graphics/player/ship_02.png']

        self.normal_animation = Animation(self.normal_state_frames, \
                                          self.ANIMATION_FPS,       \
                                          self.NORMAL_ANIMATION_CYCLIC)
        self.posx = 50
        self.posy = GameSettings.SCREENHEIGHT / 2
        ScreenObject.__init__(self, self.normal_animation,\
                                    self.posx, self.posy)
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

        ScreenObject.update(self, surface)

