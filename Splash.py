import pygame
from Engine import SplashScreen

class Splash(SplashScreen):

    def __init__(self):
        self.image = pygame.image.load('graphics/splash/splash.png')
        SplashScreen.__init__(self, self.image, 3)
