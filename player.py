import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((60, 60))
        self.image.fill('violet')
        self.rect = self.image.get_rect(topleft=pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.speed = 6

    def moving(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        elif keys[pygame.K_UP]:
            pass
        else:
            self.direction.x = 0
            self.direction.y = 0

    def update(self):
        self.moving()
        self.rect.x += self.direction.x * self.speed
