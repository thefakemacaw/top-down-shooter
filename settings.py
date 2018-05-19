#From KidsCanCode: goo.gl/t4rYbL
import pygame

#"all the colors, see the colors, make the colors, feel the colors" -Beck, 2017
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TAN = (210, 180, 140)
GRAY = (128, 128, 128)
LIGHTGRAY = (211, 211, 211)

#game options and settings
title = "Top Down Shooter"

#supersize me
width = 1024
height = 768
fps = 30
BGCOLOR = BLACK

TILESIZE = 32
GRIDWIDTH = width / TILESIZE
GRIDHEIGHT = height / TILESIZE

#wall settings
WALL_IMG = "tile_42.png"
#player settings
PLAYER_SPEED = 300
PLAYER_ROT_SPEED = 250
PLAYER_IMG = "manBlue_gun.png"
PLAYER_HIT_RECT = pygame.Rect(0, 0, 36, 36)
#mob settings
MOB_IMG = "zoimbie1_machine.png"
MOB_SPEED = 200
MOB_HIT_RECT = pygame.Rect(0, 0, 36, 36)