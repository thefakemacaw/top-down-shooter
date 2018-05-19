#from KidsCanCode blog: kidscancode.org/blog/2016/08/pygame_1-1_getting-started/ (currently on 1-4)
import pygame, random, os #import all the libraries
from settings import *

#get dat assets folder boiii (currently not used)
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "topdown")

class Player(pygame.sprite.Sprite):
    #ready player one
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join("topdown", "archer.png")).convert()
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.center = (width / 2, height / 2)
    
    def update(self):
        self.rect.x += 5
        if self.rect.left > width:
            self.rect.right = 0

#initializing the display in 5... 4... 3...
pygame.init()
#pygame.mixer.init() #for sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption(title)
clock = pygame.time.Clock()

#initialize the sprites in 5... 4... 3...
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)

#do the loop-da-loop... the game loop
running = True
while running:
    clock.tick(fps)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    #update
    all_sprites.update()

    #draw and render
    screen.fill(BLUE)
    all_sprites.draw(screen)
    #heard of a kickflip? this is it, with python
    pygame.display.flip()

pygame.quit()