import os
import sys
import math
import pygame

#check here: http://qq.readthedocs.io/en/latest/

CAPTION = "Top-Down Shooter"
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode([screen_width, screen_height])
RED = (255, 0, 0)
WHITE = (0, 0, 0)

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

''' from Mekire's "Tank Turret: Mouse" 
https://github.com/Mekire/pygame-samples/blob/master/tank_turret/turret_mouse.py '''
# class Laser(pygame.sprite.Sprite):
#     """
#     A class for our laser projectiles. Using the pygame.sprite.Sprite class
#     this time, though it is just as easily done without it.
#     """
#     def __init__(self, location, angle):
#         """
#         Takes a coordinate pair, and an angle in degrees. These are passed
#         in by the Turret class when the projectile is created.
#         """
#         pygame.sprite.Sprite.__init__(self)
#         self.original_laser = TURRET.subsurface((150,0,150,150))
#         self.angle = -math.radians(angle-135)
#         self.image = pygame.transform.rotate(self.original_laser, angle)
#         self.rect = self.image.get_rect(center=location)
#         self.move = [self.rect.x, self.rect.y]
#         self.speed_magnitude = 5
#         self.speed = (self.speed_magnitude*math.cos(self.angle),
#                       self.speed_magnitude*math.sin(self.angle))
#         self.done = False

#     def update(self, screen_rect):
#         """
#         Because pygame.Rect's can only hold ints, it is necessary to hold
#         the real value of our movement vector in another variable.
#         """
#         self.move[0] += self.speed[0]
#         self.move[1] += self.speed[1]
#         self.rect.topleft = self.move
#         self.remove(screen_rect)

#     def remove(self, screen_rect):
#         """If the projectile has left the screen, remove it from any Groups."""
#         if not self.rect.colliderect(screen_rect):
#             self.kill()


# class Control(object):
#     """Why so controlling?"""
#     def __init__(self):
#         """
#         Prepare necessities; create a Turret; and create a Group for our
#         laser projectiles.
#         """
#         self.screen = pygame.display.get_surface()
#         self.screen_rect = self.screen.get_rect()
#         self.done = False
#         self.clock = pygame.time.Clock()
#         self.fps = 60.0
#         self.keys = pygame.key.get_pressed()
#         self.cannon = playerGun((250,250))
#         self.objects = pygame.sprite.Group()

#     def event_loop(self):
#         """Events are passed on to the Turret."""
#         for event in pygame.event.get():
#             self.keys = pygame.key.get_pressed()
#             if event.type == pygame.QUIT or self.keys[pygame.K_ESCAPE]:
#                 self.done = True
#             self.cannon.get_event(event, self.objects)

#     def update(self):
#         """Update all lasers."""
#         self.objects.update(self.screen_rect)

#     def draw(self):
#         """Draw all elements to the display surface."""
#         self.screen.fill(BACKGROUND_COLOR)
#         self.cannon.draw(self.screen)
#         self.objects.draw(self.screen)

#     def display_fps(self):
#         """Show the program's FPS in the window handle."""
#         caption = "{} - FPS: {:.2f}".format(CAPTION, self.clock.get_fps())
#         pygame.display.set_caption(caption)

#     def main_loop(self):
#         """"Same old story."""
#         while not self.done:
#             self.event_loop()
#             self.update()
#             self.draw()
#             pygame.display.flip()
#             self.clock.tick(self.fps)
#             self.display_fps()


# if __name__ == "__main__":
#     os.environ['SDL_VIDEO_CENTERED'] = '1'
#     pygame.init()
#     pygame.display.set_caption(CAPTION)
#     pygame.display.set_mode(SCREEN_SIZE)
#     #image from rotmg
#     playerChar = pygame.image.load(os.path.join("archer.png")).convert()
#     TURRET.set_colorkey(COLOR_KEY)
#     run_it = Control()
#     run_it.main_loop()
#     pygame.quit()
# sys.exit()