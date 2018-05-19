#from KidsCanCode: goo.gl/oU6pkd
#import libraries
import pygame
import sys
from os import path
from settings import *
from sprites import *
from tilemap import *

class Game:
    def __init__(self):
        #initialize the game window and stuff
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        # pygame.key.set_repeat(100, 100) #continuous movement
        self.load_data()
    
    def load_data(self):
        #this puts the map.txt map data into the game
        game_folder = path.dirname(__file__)
        img_folder = path.join(game_folder, "img")
        self.map = Map(path.join(game_folder, "map.txt"))
        self.player_img = pygame.image.load(path.join(game_folder, PLAYER_IMG)).convert_alpha() #player img
        self.mob_img = pygame.image.load(path.join(game_folder, MOB_IMG)).convert_alpha() #boss img
        self.wall_img = pygame.image.load(path.join(game_folder, WALL_IMG)).convert_alpha() #wall img

    def new(self):
        #start a new game and initialize all variables
        self.all_sprites = pygame.sprite.Group()
        self.walls = pygame.sprite.Group()
        self.mobs = pygame.sprite.Group()
        #build a great wall
        for row, tiles in enumerate(self.map.data):
            #enumerate to grab the index value of an item in a list
            for col, tile in enumerate(tiles):
                if tile == "1":
                    Wall(self, col, row)
                if tile == "M":
                    Mob(self, col, row)
                if tile == "P":
                    #player spawn location
                    self.player = Player(self, col, row)
        self.camera = Camera(self.map.width, self.map.height)
    
    def run(self):
        #game loop
        self.playing = True
        while self.playing:
            self.dt = self.clock.tick(fps) / 1000
            self.events()
            self.update()
            self.draw()

    def update(self):
        #game loop update
        self.all_sprites.update()
        self.camera.update(self.player)
    
    def draw_grid(self):
        #creates a grid in game
        for x in range(0, width, TILESIZE):
            pygame.draw.line(self.screen, GRAY, (x, 0), (x, height))
        for y in range(0, height, TILESIZE):
            pygame.draw.line(self.screen, GRAY, (0, y), (width, y))

    def draw(self):
        #game loop draw
        pygame.display.set_caption("{:.2f}".format(self.clock.get_fps())) #fps in the bar on top
        self.screen.fill(BLACK)
        #self.draw_grid()
        for sprite in self.all_sprites:
            self.screen.blit(sprite.image, self.camera.apply(sprite))
        #pygame.draw.rect(self.screen, WHITE, self.player.hit_rect, 2) #was for seeing the hitbox
        pygame.display.flip()

    def events(self):
        #game loop events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    #lets you leave the game by pressing escape
                    self.quit()
                
                self.running = False
    
    def show_start_screen(self):
        #shows start screen
        pass
    
    def show_go_screen(self):
        #shows game over screen
        pass

game = Game()
game.show_start_screen()
while True:
    #what the game does when it's running
    game.new()
    game.run()
    game.show_go_screen()