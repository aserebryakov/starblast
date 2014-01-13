import sys
import random
import pygame
from pygame.locals import *
from Splash import Splash
from Player import Player
from Enemy import Enemy
from Engine import Engine

class Game:
    def __init__(self):
        self.engine = Engine()
        # Stub implementation till Background class
        # will be implemented
        self.engine.SetSplash(Splash())
        self.engine.SetBackground(None)
        self.engine.AddPlayer(Player())
        self.engine.AddEnemy(Enemy())

    def Run(self):
        self.engine.RunGame()

if __name__=='__main__':
    pygame.init()
    game = Game()
    game.Run()
