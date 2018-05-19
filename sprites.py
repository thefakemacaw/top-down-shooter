#From KidsCanCode
import pygame
from settings import *
from tilemap import collide_hit_rect
vec = pygame.math.Vector2 #vectors are used for movement and rotation

def collide_with_walls(sprite, group, dir):
    #this global function is for collision for all sprites (except walls)
    if dir == "x":
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.x > 0:
                sprite.pos.x = hits[0].rect.left - sprite.hit_rect.width / 2
            if sprite.vel.x < 0:
                sprite.pos.x = hits[0].rect.right + sprite.hit_rect.width / 2
            sprite.vel.x = 0
            sprite.hit_rect.centerx = sprite.pos.x
    if dir == "y":
        hits = pygame.sprite.spritecollide(sprite, group, False, collide_hit_rect)
        if hits:
            if sprite.vel.y > 0:
                sprite.pos.y = hits[0].rect.top - sprite.hit_rect.height / 2
            if sprite.vel.y < 0:
                sprite.pos.y = hits[0].rect.bottom + sprite.hit_rect.height / 2
            sprite.vel.y = 0
            sprite.hit_rect.centery = sprite.pos.y

class Player(pygame.sprite.Sprite):
    #creates the player sprite
    def __init__(self, game, x, y):
        self.groups = game.all_sprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.player_img
        self.rect = self.image.get_rect()
        self.hit_rect = PLAYER_HIT_RECT
        self.hit_rect.center = self.rect.center
        self.vel = vec(0, 0) #for velocity
        self.pos = vec(x, y) * TILESIZE
        self.rot = 0 #player rotation

    def get_keys(self):
        #this is for player rotation
        self.rot_speed = 0
        #this is for player movement
        self.vel = vec(0, 0)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            #moves player sprite forward
            self.vel = vec(PLAYER_SPEED, 0).rotate(-self.rot)
        if keys[pygame.K_a]:
            #rotates player sprite to the left
            self.rot_speed = PLAYER_ROT_SPEED
        if keys[pygame.K_s]:
            #moves player sprite backward at half speed
            self.vel = vec(-PLAYER_SPEED / 2, 0).rotate(-self.rot)
        if keys[pygame.K_d]:
            #rotates player sprite to the right
            self.rot_speed = -PLAYER_ROT_SPEED
    
    def update(self):
        #update player sprite
        self.get_keys()
        self.rot = (self.rot + self.rot_speed * self.game.dt) % 360
        self.image = pygame.transform.rotate(self.game.player_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.pos += self.vel * self.game.dt
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, "y")
        self.rect.center = self.hit_rect.center

class Mob(pygame.sprite.Sprite):
    #creates a class for the boss
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.mobs
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.mob_img
        self.rect = self.image.get_rect()
        self.hit_rect = MOB_HIT_RECT.copy()
        self.hit_rect.center = self.rect.center
        self.pos = vec(x, y) * TILESIZE
        self.vel = vec(0, 0) #mob velocity
        self.acc = vec(0, 0) #mob acceleration (for rotation so it doesnt instantly change direction)
        self.rect.center = self.pos
        self.rot = 0
    
    def update(self):
        #makes the mob face the player
        self.rot = (self.game.player.pos - self.pos).angle_to(vec(1, 0))
        self.image = pygame.transform.rotate(self.game.mob_img, self.rot)
        self.rect = self.image.get_rect()
        self.rect.center = self.pos
        self.acc = vec(MOB_SPEED, 0).rotate(-self.rot) #determines rotational acceleration
        self.acc += self.vel * -1 #"friction" for the mob
        self.vel += self.acc * self.game.dt #determines velocity
        self.pos = self.vel * self.game.dt + 0.5 * self.acc * self.game.dt ** 2 #determines position
        self.hit_rect.centerx = self.pos.x
        collide_with_walls(self, self.game.walls, "x")
        self.hit_rect.centery = self.pos.y
        collide_with_walls(self, self.game.walls, "y")
        self.rect.center = self.hit_rect.center

class Wall(pygame.sprite.Sprite):
    #creates a class for a wall sprite
    def __init__(self, game, x, y):
        self.groups = game.all_sprites, game.walls
        pygame.sprite.Sprite.__init__(self, self.groups)
        self.game = game
        self.image = game.wall_img
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.x = x * TILESIZE
        self.rect.y = y * TILESIZE
