
from math import pi, cos, sin
import pygame

class Ship():
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)

        self.image = pygame.image.load("fleet.jpg")
        self.image = pygame.transform.scale(self.image, (50, 25))
        self.rect = self.image.get_rect()

        self.speed = 0.3
        self.direction = 0.5 * pi
        self.position = [100, 100]

        self.image = pygame.transform.rotate(self.image, self.direction * 360 / (-2 * pi))

    def update(self):
        x, y = (1, 0)
        a = self.direction
        rot = (x * cos(a) - y * sin(a), x * sin(a) + y * cos(a))
        self.position = (self.position[0] + self.speed * rot[0],
                         self.position[1] + self.speed * rot[1])
        print(self.direction)
        