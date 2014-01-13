import pygame
from ScreenObject import ScreenObject
from GameSettings import GameSettings

class SplashScreen(pygame.Surface):

    def __init__(self, image, splashTime):
        pygame.Surface.__init__(self,\
                         (GameSettings.SCREENWIDTH, GameSettings.SCREENHEIGHT), \
                         0, 32)
        self.blit(image, (0,0))
        self.splashTime = splashTime
