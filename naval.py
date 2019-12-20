import pygame
import tmx


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super(Player, self).__init__(*groups)
        
        self.image = pygame.image.load("images_pygame/body.png")
        s = 50/518
        self.image = pygame.transform.scale(self.image, (round(400 * s), round(518 * s)))
        
        self.rect = pygame.rect.Rect((320, 240), self.image.get_size())

        self.resting = False
        self.dy = 0

    def update(self, dt, game):
        last = self.rect.copy()
        key = pygame.key.get_pressed()
        if key[pygame.K_LEFT]:
            self.rect.x -= 300 * dt
        if key[pygame.K_RIGHT]:
            self.rect.x += 300 * dt
        # if key[pygame.K_UP]:
        #     self.rect.y -= 300 * dt
        # if key[pygame.K_DOWN]:
        #     self.rect.y += 300 * dt
        if self.resting and key[pygame.K_SPACE]:
            self.dy = -500
        self.dy = min(400, self.dy + 40)

        self.rect.y += self.dy * dt

        new = self.rect
        self.resting = False
        for cell in pygame.sprite.spritecollide(self, game.walls, False):
            self.rect = last
            cell = cell.rect
            if last.right <= cell.left and new.right > cell.left:
                new.right = cell.left
            if last.left >= cell.right and new.left < cell.right:
                new.left = cell.right
            if last.bottom < cell.top and new.bottom > cell.top:
                self.resting = True
                new.bottom = cell.top
                self.dy = 0
            if last.top >= cell.bottom and new.top < cell.bottom:
                new.top = cell.bottom
                self.dy = 0
        self.groups()[0].camera_x = self.rect.x - 320

class ScrolledGroup(pygame.sprite.Group):
    def draw(self, surface):
        for sprite in self.sprites():
            surface.blit(sprite.image, (sprite.rect.x - self.camera_x, sprite.rect.y))


class Game():
    def main(self, screen):
        clock = pygame.time.Clock()

        background = pygame.image.load("images/bg.png")
        
        # image = pygame.image.load("images_pygame/body.png")
        # s = 50/518
        # image = pygame.transform.scale(image, (round(400 * s), round(518 * s)))
        # sprites = pygame.sprite.Group()

        # sprites = ScrolledGroup()
        # sprites.camera_x = 0
        # self.player = Player(sprites)
        # self.walls = pygame.sprite.Group()
        # block = pygame.image.load("images_pygame/darkDirtBlock.png")
        # for x in range(0, 800, 32):
        #     for y in range(0, 480, 32):
        #         if x in (0, 800 - 32) or y in (0, 480 - 32):
        #             wall = pygame.sprite.Sprite(self.walls)
        #             wall.image = block
        #             wall.rect = pygame.rect.Rect((x, y), block.get_size())
        # sprites.add(self.walls)
        self.tilemap = tmx.load("map.tmx", screen.get_size())

        self.sprites = tmx.SpriteLayer()
        start_cell = self.tilemap.layers["triggers"].find("player")[0]
        self.player = Player((start_cell.px, start_cell.py), self.sprites)
        self.tilemap.layers.append(self.sprites)

        while True:
            dt = clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return
                if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    return
            
            # image_x += 1
            
            sprites.update(dt/1000, self)
            screen.fill(((200, 200, 200)))
            screen.blit(background, (0, 0))
            # screen.blit(image, (image_x, image_y))
            sprites.draw(screen)
            pygame.display.flip()

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    Game().main(screen)