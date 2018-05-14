import configparser
import os
import sys
import math
import pygame

#The class represents the enemy Block Zombies
class blockZombie(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()
        self.image = pygame.Surface([width, height])
        self.image.fill(RED)
        self.image.set_colorkey(RED)
        pygame.draw.square(self.image, color, [width, height])
        self.rect

#The class represents the player
class playerSprite(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("archer.png").convert()
        self.image.set_colorkey(WHITE)