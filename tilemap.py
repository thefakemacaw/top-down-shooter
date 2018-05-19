#From KidsCanCode (again - link in the main file)
import pygame
from settings import *

def collide_hit_rect(one, two):
    #sees collision
    return one.hit_rect.colliderect(two.rect)

class Map:
    #draws the map
    def __init__(self, filename):
        self.data = []
        with open(filename, "rt") as f:
            for line in f:
                self.data.append(line.strip())
    
        self.tilewidth = len(self.data[0])
        self.tileheight = len(self.data)
        self.width = self.tilewidth * TILESIZE
        self.height = self.tileheight * TILESIZE

class Camera:
    #creates a camera that follows the player around
    def __init__(self, width, height):
        self.camera = pygame.Rect(0, 0, width, height)
        self.width = width
        self.height = height
    
    def apply(self, entity):
        #gives us a new rectangle that is shiftd by the amount in (self.camera.topleft)
        return entity.rect.move(self.camera.topleft)
    
    def update(self, target):
        #shifts the map in the opposite direction the player is moving
        x = -target.rect.centerx + int(width / 2)
        y = -target.rect.centery + int(height / 2)

        #limit scrolling to map size
        x = min(0, x) #left side
        y = min(0, y) #top side
        x = max(-(self.width - width), x) #right side
        y = max(-(self.height - height), y) #bottom side

        self.camera = pygame.Rect(x, y, self.width, self.height)