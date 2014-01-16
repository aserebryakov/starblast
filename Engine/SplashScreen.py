import pygame
from ScreenObject import ScreenObject
from GameSettings import GameSettings

class SplashScreen:

    def __init__(self, image, splashTime):
        self.surf = pygame.Surface((GameSettings.SCREENWIDTH, GameSettings.SCREENHEIGHT), \
                         0, 32)
        self.surf.blit(image, (0,0))
        self.splashTime = splashTime
