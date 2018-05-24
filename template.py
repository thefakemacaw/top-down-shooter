#from KidsCanCode blog: kidscancode.org/blog/2016/08/pygame_1-1_getting-started/
#this code is the template that I used to write the rest of my code
import pygame, random #import all the libraries

#supersize me
width = 800
height = 600
fps = 30

#"all the colors, see the colors, make the colors, feel the colors" -Beck, 2017
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#initializing the display in 5... 4... 3...
pygame.init()
#pygame.mixer.init() #for sound
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Definitely Not the Public Test Server")
clock = pygame.time.Clock()

#initialize the sprites in 5... 4... 3...
all_sprites = pygame.sprite.Group()

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
    screen.fill(BLACK)
    all_sprites.draw(screen)
    #heard of a kickflip? this is it, with python
    pygame.display.flip()

pygame.quit()