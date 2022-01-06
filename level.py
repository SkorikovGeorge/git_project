import pygame
from levels_tiles import Tile
from level_info import tile_size, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


class Level:
    def __init__(self, level_map_data, surface):
        self.tiles_sprite_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.level_building(level_map_data)
        self.map_shift_x = 0
        self.map_shift_y = 0

    def level_building(self, map_data):
        for row_index, row in enumerate(map_data):
            for col_index, column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == 'X':
                    tile = Tile((x, y), tile_size)
                    self.tiles_sprite_group.add(tile)
                if column == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)

    def camera_scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < (SCREEN_WIDTH / 4) and direction_x < 0:
            self.map_shift_x = 8
            player.speed = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.map_shift_x = -8
            player.speed = 0
        else:
            self.map_shift_x = 0
            player.speed = 8
        self.tiles_sprite_group.update(self.map_shift_x, 'x')

    def camera_scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        if player_y < (SCREEN_HEIGHT / 4) and direction_y < 0:
            self.map_shift_y = 8
            player.speed = 0
        elif player_y > SCREEN_HEIGHT - (SCREEN_HEIGHT / 4) and direction_y > 0:
            self.map_shift_y = -8
            player.speed = 0
        else:
            self.map_shift_y = 0
            player.speed = 8
        self.tiles_sprite_group.update(self.map_shift_y, 'y')

    def vertical_move(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed
        for sprite in self.tiles_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

    def horizontal_move(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        for sprite in self.tiles_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def run(self):
        self.tiles_sprite_group.draw(self.display_surface)
        self.player.update()
        self.camera_scroll_x()
        self.camera_scroll_y()
        self.horizontal_move()
        self.vertical_move()
        self.player.draw(self.display_surface)
