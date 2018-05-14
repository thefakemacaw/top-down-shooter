#based on code from http://usingpython.com/pygame-images/

import pygame, sys, os, random

#imports the pygame.locals library
from pygame.locals import *

#tile creation
#represents colors
BLUE = (0,0,255)
BROWN = (153,76,0)
BLACK = (0,0,0)
RED = (255,0,0)

#defines the parts of a map (bomb is my own type of tile)
WALL = 0
FLOOR = 1
WATER = 2
BOMB = 3

#was for getting images for each tile
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "topdown")

"""************************************classes***********************************"""
#from Seth Kenlon's tutorial on sprites https://opensource.com/article/17/12/game-python-add-a-player
#the player sprite (image from realm of the mad god)
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("topdown", "archer.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()
    def control(self, x, y):
        #controls player movement
        self.movex += x
        self.movey += y
    def update(self):
        #updates sprite position
        self.rectx = self.rect.x + self.movex
        self.recty = self.rect.y + self.movey

#boss class (image from rotmg as well)
class Boss(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 0
        self.movey = 0
        self.frame = 0
        self.images = []
        img = pygame.image.load(os.path.join("topdown", "boss.png")).convert()
        self.images.append(img)
        self.image = self.images[0]
        self.rect = self.image.get_rect()

"""**************************************game setup****************************************"""
#dictionary to pair the tiles with a color
textures = {
    WALL: BLACK,
    FLOOR: BROWN,
    WATER: BLUE,
    BOMB: RED
}

#game dimensions
TILESIZE = 40
MAPWIDTH = 20
MAPHEIGHT = 15

tiles = [WALL, FLOOR, WATER]

tilemap = [[FLOOR for w in range(MAPWIDTH)] for h in range(MAPHEIGHT)]

#set up display
pygame.init()
DISPLAY = pygame.display.set_mode((MAPWIDTH*TILESIZE, MAPHEIGHT*TILESIZE))
DISPLAYBOX = DISPLAY.get_rect()
pygame.display.set_caption("Top Down Shooter")

#rng-sus for tiles, looping through each row
for rw in range(MAPHEIGHT):
    #loops through each column in the row
    for cl in range(MAPWIDTH):
        #rn-jesus
        randomNumber = random.randint(0, 30)
        #tile is wall if randomNumber is 0 or 1
        if randomNumber == 0 or randomNumber == 1 or randomNumber == 2:
            tile = WALL
        #tile is water if randomNumber is 2, 3, or 4
        elif randomNumber == 3 or randomNumber == 4 or randomNumber == 5:
            tile = WATER
        elif randomNumber == 6:
            tile = BOMB
        else:
            tile = FLOOR
        #sets the position in the tilemap to the chosen tile
        tilemap[rw][cl] = tile

#from Seth Kenlon's tutorial on sprites https://opensource.com/article/17/12/game-python-add-a-player
#gets the player sprite to appear at (0,0)
player = Player()
player.rect.x = 0
player.rect.y = 0
player_list = pygame.sprite.Group()
player_list.add(player)
steps = 10
#gets the boss sprite to appear at (400,300)
# boss = Boss()
# boss.rect.x = 400
# boss.rect.y = 300
# boss_list = pygame.sprite.Group()
# boss_list.add(boss)

"""***************************************main loop**************************************"""
while True:
    #gets user events, such as quitting the game
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        #from Seth Kenlon https://opensource.com/article/17/12/game-python-moving-player
        #this prints what happens when you press the directional keys (WASD or arrows)
        elif event.type == pygame.KEYDOWN:
            if event.key == ord("w") or event.key == K_UP:
                player.control(0, steps)
                print("up")
            if event.key == ord("a") or event.key == K_LEFT:
                player.control(-steps, 0)
                print("left")
            if event.key == ord("s") or event.key == K_DOWN:
                player.control(0, -steps)
                print("down")
            if event.key == ord("d") or event.key == K_RIGHT:
                player.control(steps, 0)
                print("right")
        elif event.type == pygame.KEYUP:
            if event.key == ord("w") or event.key == K_UP:
                player.control(0, steps)
                print("up stop")
            if event.key == ord("a") or event.key == K_LEFT:
                player.control(-steps, 0)
                print("left stop")
            if event.key == ord("s") or event.key == K_DOWN:
                player.control(0, -steps)
                print("down stop")
            if event.key == ord("d") or event.key == K_RIGHT:
                player.control(steps, 0)
                print("right stop")
    player.update()
    player_list.draw(DISPLAY)
    #boss_list.draw(DISPLAY)
    pygame.display.update()

    #loops through each row
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            #draws the tile in its respective position
            pygame.draw.rect(DISPLAY, textures[tilemap[row][column]], (column*TILESIZE, row*TILESIZE, TILESIZE, TILESIZE))