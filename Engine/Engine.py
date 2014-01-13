import sys
import random
import pygame
import copy
from pygame.locals import *
from ScreenObject import ScreenObject
from GameSettings import GameSettings

class Engine:

    def __init__(self):
        self.DISPLAYSURF = pygame.display.set_mode((GameSettings.SCREENWIDTH,\
                                            GameSettings. SCREENHEIGHT), 0, 32)
        self.playerGroup = pygame.sprite.Group()
        self.enemyGroup  = pygame.sprite.Group()
        self.fpsClock    = pygame.time.Clock()
        self.playerTypes = []
        self.players     = []
        self.enemyTypes  = []
        self.bullets     = []
        self.background  = None
        self.splash      = None
        self.start_screen= None
        self.end_screen  = None

    def RegisterPlayerType(self, player):
        assert issubclass(player, ScreenObject)
        self.playerTypes.append(player)

    def RegisterEnemyType(self, enemy):
        assert issubclass(enemy, ScreenObject)
        self.enemyTypes.append(enemy)

    def CreatePlayers(self):
        for playerType in self.playerTypes:
            player = playerType()
            self.players.append(player)
            self.playerGroup.add(player)

    def SetBackground(self, background):
        self.background = pygame.Surface(self.DISPLAYSURF.get_size(),\
                                         0, 32)
        self.background.fill(GameSettings.BACKGROUND_COLOR)

    def SetSplash(self, splash):
        pass

    def SetStartScreen(self, splash):
        pass

    def SetEndScreen(self, endscreen):
        pass

    def ShowSplash(self):
        pass

    def ShowStartScreen(self):
        pass

    def ShowEndScreen(self):
        pygame.quit()
        sys.exit()

    def HandleCollisions(self, sprites):
        for sprite in sprites:
            sprite.kill()

    def GenerateEnemy(self):
        rand = random.Random()

        if rand.uniform(0, 1) < GameSettings.ENEMY_CHANCE:
            # TODO: Implement enemy type chosing
            # NOTE: Looks like a workaround
            newEnemy = self.enemyTypes[0]() 

            # Initialize new parameters
            newEnemy.posy = rand.uniform(0, GameSettings.SCREENHEIGHT)
            newEnemy.posx = GameSettings.SCREENWIDTH
            newEnemy.dx   = rand.uniform(10, 30)
            newEnemy.dy   = rand.uniform(-10, 10)
            self.enemyGroup.add(newEnemy)

    def GameLoop(self):
        running = True
        while running:
            self.DISPLAYSURF.blit(self.background, (0, 0))

            for event in pygame.event.get():
                if event.type == QUIT:
                    running = False
                elif event.type == KEYDOWN and event.key == K_ESCAPE:
                    running = False

            self.GenerateEnemy()
            self.playerGroup.update(self.DISPLAYSURF)
            self.enemyGroup.update(self.DISPLAYSURF)
            self.playerGroup.draw(self.DISPLAYSURF)
            self.enemyGroup.draw(self.DISPLAYSURF)

            for player in self.players:
                collisions = pygame.sprite.spritecollide(player, self.enemyGroup,\
                                        False, \
                                        pygame.sprite.collide_circle)
                self.HandleCollisions(collisions)
            pygame.display.update()
            self.fpsClock.tick(GameSettings.FPS)


    def RunGame(self):
        self.ShowSplash()
        self.ShowStartScreen()
        self.CreatePlayers()
        self.GameLoop()
        self.ShowEndScreen()

