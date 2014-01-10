import sys
import random
import pygame
from pygame.locals import *
from Player import Player
from Enemy import Enemy
from Engine import GameSettings 

class Game:
    running = True
    playerGroup = pygame.sprite.Group()
    enemyGroup  = pygame.sprite.Group()
    fpsClock    = pygame.time.Clock()
    player      = Player()
    DISPLAYSURF = None

    def __init__(self):
        self.DISPLAYSURF = pygame.display.set_mode((GameSettings.SCREENWIDTH,\
                                            GameSettings. SCREENHEIGHT), 0, 32)
        self.playerGroup.add(self.player)

    def GenerateEnemy(self):
        rand = random.Random()

        if rand.uniform(0, 1) < GameSettings.ENEMY_CHANCE:
            newEnemy = Enemy()
            self.enemyGroup.add(newEnemy)

    def Run(self):
        while self.running:
            self.DISPLAYSURF.fill(GameSettings.BACKGROUND_COLOR)

            for event in pygame.event.get():
                if event.type == QUIT:
                    self.running = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    self.running = False

            self.GenerateEnemy()
            self.playerGroup.update(self.DISPLAYSURF)
            self.enemyGroup.update(self.DISPLAYSURF)
            pygame.sprite.spritecollide(self.player, self.enemyGroup,\
                                        True, pygame.sprite.collide_circle)
            pygame.display.update()
            self.fpsClock.tick(GameSettings.FPS)

        pygame.quit()
        sys.exit()

if __name__=='__main__':
    pygame.init()
    game = Game()
    game.Run()
