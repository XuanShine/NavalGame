import sys, pygame
from pygame import Color, Rect
from math import cos, sin, pi, acos, sqrt
from random import randrange

import logging

from Movable import Movable
from operation_on_vector import *
from config import *
import main


# TODO: faire attention au fichier de logs
logging.basicConfig(filename="main.log", level=logging.DEBUG,
                    format="%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")


class Missile(Movable):

    def __init__(self, position, speed, target, power_range, damage, game, *groups):

        v = target[0] - position[0], target[1] - position[1]  # (xb - xa, yb - ya)
        direction = getAngleDegFromVector((1, 0), v)

        x, y = main.raw_missile_image.get_size()
        SIZE_X =  10
        size_y = round(y / x * SIZE_X)
        size = SIZE_X, size_y

        super().__init__(position, speed, direction, size, *groups)

        self.game = game
        
        self.main_image = pygame.transform.smoothscale(main.raw_missile_image, size)
        self.main_image = pygame.transform.rotate(self.main_image, -90)
        self.image = pygame.transform.rotate(self.main_image, -self.direction)

        self.explode_image = pygame.transform.smoothscale(main.raw_explode_image, (power_range, power_range))
        self.power_range = power_range  # MissileSurface
        self.damage = damage
        self.exploded = False
        self.target = target
        self.life_explosion = 0.5  # in seconds # MissileSurface
        self.last_distance = distancePoints(position, target)
    
    def update(self, dt):
        super().update(dt)
        if not self.exploded:
            distance_from_target = distancePoints((self.x, self.y), self.target)
            if distance_from_target > self.last_distance:
                self.exploded = True
                self.direction = 0
                self.speed = 0
                self.rect = Rect((self.x, self.y), (self.power_range, self.power_range))
                self.image = self.explode_image
                self.game.missiles.remove(self)
                touched = pygame.sprite.spritecollide(self, self.game.all_sprites,  False)
                if touched:
                    ship = touched[0]
                    ship.life -= self.damage
                    self.exploded = True
                    self.game.explosions.add(self)
                else:
                    # afficher un "plouc" dans l’eau.
                    pass
            else:
                self.last_distance = distance_from_target
        elif self.exploded and self.life_explosion > 0:
            self.life_explosion -= dt
        elif self.exploded and self.life_explosion <= 0:
            self.game.explosions.remove(self)



class MissileDeSurface(Missile):
    def update(self, dt):
        super().update(dt)
        if not self.exploded:
            distance_from_target = distancePoints((self.x, self.y), self.target)
            if distance_from_target > self.last_distance:
                self.exploded = True
                self.direction = 0
                self.speed = 0
                self.rect = Rect((self.x, self.y), (self.power_range, self.power_range))
                self.image = self.explode_image
                self.game.missiles.remove(self)
                self.game.explosions.add(self)
            else:
                self.last_distance = distance_from_target
        elif self.exploded and self.life_explosion > 0:
            self.life_explosion -= dt
        elif self.exploded and self.life_explosion <= 0:
            self.game.explosions.remove(self)