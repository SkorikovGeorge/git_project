import pygame
from level_info import  tile_size

class Money(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((tile_size * 0.4, tile_size * 0.4))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(topleft=pos)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
