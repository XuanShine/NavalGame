import sys, pygame
from pygame import Color, Rect
from math import cos, sin, pi, acos, sqrt
from random import randrange

class Movable(pygame.sprite.Sprite):
    def __init__(self, position, speed, direction, size, *groups):
        super(Movable, self).__init__(*groups)

        self.x, self.y = position  # rect.x,y convert float to int values.
        self.speed = speed
        self.direction = direction
        self.rect = Rect(position, size)
    
    def _move(self, dt):
        # Processing
        move_x = cos(self.direction / 360 * 2 * pi) * self.speed * dt
        move_y = sin(self.direction / 360 * 2 * pi) * self.speed * dt
        self.x += move_x
        self.y += move_y
        self.rect.x = self.x
        self.rect.y = self.y
    
    def _action(self):
        pass

    def update(self, dt):
        self._action()
        self._move(dt)