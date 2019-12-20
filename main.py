import sys, pygame
from pygame import Color, Rect
from math import cos, sin, pi, acos, sqrt
from random import randrange

import logging

from Movable import Movable

from config import *


# TODO: faire attention au fichier de logs
logging.basicConfig(filename="main.log", level=logging.DEBUG,
                    format="%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")


class Game():
    def main(self, screen):
        clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()

        ship = Ship((10, 10), game=self)
        for i in range(3):
            IA_Ship((randrange(WIDTH), randrange(HEIGHT)), randrange(25, 75), randrange(360), self, self.all_sprites)
        self.all_sprites.add(ship)
        self.missiles = pygame.sprite.Group()
        self.explosions = pygame.sprite.Group()

        for i in range(150):
            Missile((randrange(WIDTH), randrange(HEIGHT)), randrange(50, 150), (randrange(700), randrange(500)), randrange(10, 60), 1, self, self.missiles)

        while True:
            dt = clock.tick(FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return

            # Processing
            self.missiles.update(dt/1000)
            self.explosions.update(dt/1000)
            self.all_sprites.update(dt / 1000)

            # draw
            screen.fill((0,119,190))
            self.all_sprites.draw(screen)
            self.missiles.draw(screen)
            self.explosions.draw(screen)
            pygame.display.flip()



successes, failures = pygame.init()
logging.info(f"{successes} successes and {failures} failures")
pygame.mixer.init()

pygame.display.set_caption("Bataille Navale")
screen = pygame.display.set_mode(SIZE)

missile_image = "images/missile.png"
raw_missile_image = pygame.image.load(missile_image).convert()
explode_image = "images/explosion.png"
raw_explode_image = pygame.image.load(explode_image).convert()
ship_image = "images/ship.jpg"
raw_ship_image = pygame.image.load(ship_image).convert()

try:
    from Ship import Ship, IA_Ship
except ImportError:
    # Ship module importé une seconde fois => on ignore l’import.
    pass
try:
    from Missile import Missile
except ImportError:
    # Missile module importé une seconde fois => on ignore l’import.
    pass

if __name__ == "__main__":
    Game().main(screen)