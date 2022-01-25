import pygame
import random

tile_image = pygame.image.load('images/tile_image/метеорит.png')
tile_image_1 = pygame.image.load('images/tile_image/метеорит1.png')
tile_image_2 = pygame.image.load('images/tile_image/метеорит2.png')
tile_image_3 = pygame.image.load('images/tile_image/метеорит3.png')
lava_tile_image = pygame.image.load('images/tile_image/горячий_метеорит.png')
tile_images = [tile_image, tile_image_1, tile_image_2, tile_image_3]


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size, visibility):
        super().__init__()
        if visibility == 1:
            self.image = pygame.Surface((size, size))
            self.rect = self.image.get_rect(topleft=position)
        else:
            image_number = random.randint(1, 4)
            self.image = pygame.transform.scale(tile_images[image_number - 1], (size, size))
            self.rect = self.image.get_rect(topleft=position)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
