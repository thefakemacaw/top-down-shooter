#based on code from http://usingpython.com/pygame-images/

import pygame, sys, os

#imports the pygame.locals library
from pygame.locals import *

#tile creation
#represents colors
BLUE = (0,0,255)
BROWN = (153,76,0)
BLACK = (0,0,0)

#defines the parts of a map
WALL = 0
FLOOR = 1
WATER = 2

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "topdown")

#dictionary to pair the tiles with a color
textures = {
    WALL: BLACK,
    FLOOR: pygame.image.load(os.path.join(img_folder, "floor.png")).convert(),
    WATER: pygame.image.load(os.path.join(img_folder, "water.gif")).convert()
}

tilemap = [
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, WATER, WATER, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, WATER, WATER, WATER, FLOOR, WALL],
    [WALL, FLOOR, WATER, WATER, WATER, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, WATER, WATER, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, FLOOR, WALL],
    [WALL, WALL, WALL, WALL, WALL, WALL, WALL, WALL]
]

#game dimensions
TILESIZE = 40
MAPWIDTH = 8
MAPHEIGHT = 8

#set up display
pygame.init()

DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
pygame.display.set_caption("Top Down Shooter")

#establishes the "main" loop
while True:
    #gets user events, such as quitting the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    #loops through each row
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #draws the tile in its respective position
            pygame.draw.rect(DISPLAY, textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))
    pygame.display.update()