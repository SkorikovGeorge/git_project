import pygame
from levels_tiles import Tile
from level_info import tile_size


class Level:
    def __init__(self, level_map_data, surface):
        self.tiles_sprite_group = pygame.sprite.Group()
        self.display_surface = surface
        self.level_building(level_map_data)
        self.map_shift = 0

    def level_building(self, map_data):
        for row_index, row in enumerate(map_data):
            for col_index, column in enumerate(row):
                if column == 'X':
                    x = col_index * tile_size
                    y = row_index * tile_size
                    tile = Tile((x, y), tile_size)
                    self.tiles_sprite_group.add(tile)

    def run(self):
        self.tiles_sprite_group.update(self.map_shift)
        self.tiles_sprite_group.draw(self.display_surface)
