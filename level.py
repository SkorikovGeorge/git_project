import pygame
from levels_tiles import Tile
from level_info import tile_size
from player import Player


class Level:
    def __init__(self, level_map_data, surface):
        self.tiles_sprite_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.display_surface = surface
        self.level_building(level_map_data)
        self.map_shift = 0

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

    def vertical_move(self):
        player = self.player.sprite
        player.add_gravity()
        for sprite in self.tiles_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0

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
        self.tiles_sprite_group.update(self.map_shift)
        self.tiles_sprite_group.draw(self.display_surface)
        self.player.update()
        self.horizontal_move()
        self.vertical_move()
        self.player.draw(self.display_surface)