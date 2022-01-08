import pygame

tile_image = pygame.image.load('images/tile_image/метеорит.png')


class Tile(pygame.sprite.Sprite):
    def __init__(self, position, size, visibility):
        super().__init__()
        if visibility == 1:
            self.image = pygame.Surface((size, size))
            self.rect = self.image.get_rect(topleft=position)
        else:
            self.image = pygame.transform.scale(tile_image, (size, size))
            self.rect = self.image.get_rect(topleft=position)

    def update(self, shift, direction):
        if direction == 'x':
            self.rect.x += shift
        elif direction == 'y':
            self.rect.y += shift
