import pygame


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((152, 251, 152))
        self.rect = self.image.get_rect(topleft=position)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
