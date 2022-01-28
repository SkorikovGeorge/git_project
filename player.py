import pygame
from levels_info import tile_size

player_spaceship_image = pygame.image.load('date/images/spaceship_images/корабль выкл.png')
player_diagonal_spaceship_image = pygame.image.load('date/images/spaceship_images/корабль диагональ выкл.png')


class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.transform.scale(player_spaceship_image, (tile_size * 0.8, tile_size * 0.8))
        self.rect = self.image.get_rect(topleft=pos)

        # повороты изображения корабля
        self.spaceship_up = self.image
        self.spaceship_down = pygame.transform.flip(self.image, False, True)
        self.spaceship_left = pygame.transform.rotate(self.image, 90)
        self.spaceship_right = pygame.transform.rotate(self.image, -90)

        self.spaceship_up_and_right = pygame.transform.rotate(self.image, -45)
        self.spaceship_up_and_left = pygame.transform.rotate(self.image, 45)
        self.spaceship_down_and_right = pygame.transform.rotate(self.image, -135)
        self.spaceship_down_and_left = pygame.transform.rotate(self.image, 135)

        self.direction = pygame.math.Vector2(0, 0)
        self.speed_x = 8
        self.speed_y = 8

    def moving(self):
        # движение игрока по нажатию клавиш
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0
        if keys[pygame.K_UP]:
            self.direction.y = -1
        elif keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

    def rotate_player_sprite(self):
        # повороты изображения игрока
        if self.direction.y == 1:
            self.image = self.spaceship_down
        elif self.direction.y == -1:
            self.image = self.spaceship_up
        elif self.direction.x == 1:
            self.image = self.spaceship_right
        elif self.direction.x == -1:
            self.image = self.spaceship_left

    def update(self):
        self.moving()
        self.rotate_player_sprite()
