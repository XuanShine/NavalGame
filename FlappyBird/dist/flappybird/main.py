import sys, pygame
from pygame import Color
from math import cos, sin, pi

import logging

from Ship import Ship

# TODO: faire attention au fichier de logs
logging.basicConfig(filename="main.log", level=logging.DEBUG,
                    format="%(asctime)s -- %(name)s -- %(levelname)s -- %(message)s")

SIZE = WIDTH, HEIGHT = 800, 600
FPS = 60


successes, failures = pygame.init()
logging.info(f"{successes} successes and {failures} failures")
pygame.mixer.init()

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption("Bataille Navale")
clock = pygame.time.Clock()


all_sprites = pygame.sprite.Group()

ship = Ship()
# all_sprites.add(ship)

# breakpoint()

while True:
    clock.tick(FPS)
    new_image = ship.image
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.direction = (ship.direction + 0.5) % (2 * pi)
                new_image = pygame.transform.rotate(ship.image, ship.direction * 360 / (-2 * pi))
            elif event.key == pygame.K_LEFT:
                ship.direction = (ship.direction - 0.5) % (2 * pi)
                new_image = pygame.transform.rotate(ship.image, ship.direction * 360 / (-2 * pi))
    

    all_sprites.update()
    ship.update()
    screen.fill(Color(0, 119, 190))
    screen.blit(new_image, ship.position)
    pygame.display.flip()
    # breakpoint()