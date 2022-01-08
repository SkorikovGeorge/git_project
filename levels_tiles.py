import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
