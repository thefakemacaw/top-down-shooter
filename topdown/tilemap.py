import pygame, sys, os
#represents colors
BLUE = (0,0,255)
BROWN = (153,76,0)
WHITE = (0,0,0)

#defines the parts of a map
WALL = 0
FLOOR = 1
WATER = 2

#dictionary to pair the tiles with a color
colors = {
    WALL: WHITE,
    FLOOR: BROWN,
    WATER: BLUE
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

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.movex = 10
        self.movey = 10
        self.vx = 0
        self.vy = 0
        img = pygame.image.load(os.path.join("topdown", "archer.png"))
    def event(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                self.vy = 1
            elif event.key == pygame.K_LEFT:
                self.vx = -1
            elif event.key == pygame.K_DOWN:
                self.vy = -1
            elif event.key == pygame.K_RIGHT:
                self.vy = 1
        if event.type == pygame.KEYUP:
                        if event.key == pygame.K_UP:
                self.vy = 1
            elif event.key == pygame.K_LEFT:
                self.vx = -1
            elif event.key == pygame.K_DOWN:
                self.vy = -1
            elif event.key == pygame.K_RIGHT:
                self.vy = 1