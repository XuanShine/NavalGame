
from math import pi, cos, sin
import pygame
import sys

from config import *

from Missile import Missile
from Movable import Movable
import main


class Ship(Movable):
    def __init__(self, position, speed=35, direction=0, game=None, *groups):

        x, y = main.raw_ship_image.get_size()
        SIZE_X =  100
        size_y = round(y / x * SIZE_X)
        size = SIZE_X, size_y

        super().__init__(position, speed, direction, size, *groups)

        self.main_image = pygame.transform.smoothscale(main.raw_ship_image, size)
        self.image = pygame.transform.rotate(self.main_image, -self.direction)
        self.max_speed = 100
        self.game = game
        self.life = 100
        
    def _action(self):
        # User inputs
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.direction -= 1
        if key[pygame.K_RIGHT]:
            self.direction += 1
        if key[pygame.K_UP]:
            self.speed += 10
            self.speed = min(self.speed, self.max_speed)
        if key[pygame.K_DOWN]:
            self.speed -= 10
            self.speed = max(self.speed, -self.max_speed/4)  # vitesse max en recule / 
        if pygame.mouse.get_pressed()[0]:
            target = pygame.mouse.get_pos()
            missile = Missile((self.x, self.y), 130, target, 30, 5, self.game)
            self.game.missiles.add(missile)

    def update(self, dt):
        # action, move
        super().update(dt)

        # Rotate
        self.image = pygame.transform.rotate(self.main_image, -self.direction)


class IA_Ship(Ship):
    def __init__(self, position, speed, direction= 30, game=None, *groups):
        super().__init__(position, speed, direction, game, *groups)
    
    def _action(self):
        self.direction = self.direction % 360
        if ((self.rect.left < 0 and 90 < self.direction < 270) or
            (self.rect.right > WIDTH and
            (self.direction < 90 or self.direction > 270))):
            self.direction = -self.direction + 180
        if ((self.rect.top < 0 and 180 < self.direction < 360) or
            (self.rect.bottom > HEIGHT and 0 < self.direction < 180)):
            self.direction = -self.direction
        
