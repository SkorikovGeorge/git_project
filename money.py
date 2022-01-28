import pygame
import random

from levels_info import tile_size

# подгрузка изображений мусора
garbage_image_1 = pygame.image.load('data/images/garbage_image/банка.png')
garbage_image_2 = pygame.image.load('data/images/garbage_image/молоко.png')
garbage_image_3 = pygame.image.load('data/images/garbage_image/банан.png')
garbage_image_4 = pygame.image.load('data/images/garbage_image/мыло.png')
garbage_image_5 = pygame.image.load('data/images/garbage_image/зеленый мешок.png')
garbage_images = [garbage_image_1, garbage_image_2, garbage_image_3, garbage_image_4, garbage_image_5]


class Money(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # рандомный выбор изображений
        image_number = random.randint(1, 5)
        self.image = pygame.transform.scale(garbage_images[image_number - 1], (tile_size * 0.65, tile_size * 0.65))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
