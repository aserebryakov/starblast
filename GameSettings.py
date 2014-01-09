import pygame
from pygame.locals import *

class Colors:
    BLACK = pygame.Color(0,0,0)
    WHITE = pygame.Color(255, 255, 255)
    BLUE  = pygame.Color(60, 60, 200)

class GameSettings:
    SCREENWIDTH = 800
    SCREENHEIGHT = 600
    BACKGROUND_COLOR = Colors.BLUE
    FPS = 30
    ENEMY_CHANCE = 0.2
