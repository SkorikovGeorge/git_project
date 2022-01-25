import pygame
from levels_tiles import Tile
from level_info import tile_size, SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player
from money import Money


class Level:
    def __init__(self, level_map_data, surface):
        self.tiles_sprite_group = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.money_sprite_group = pygame.sprite.Group()
        self.lava_tiles_group = pygame.sprite.Group()
        self.display_surface = surface
        self.money_quantity = 0
        self.level_building(level_map_data)
        self.map_shift_x = 0
        self.map_shift_y = 0

        self.background_coordinate_x = -200
        self.background_coordinate_y = -200
        self.background_image = pygame.image.load('images/space_image/space_background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (
            self.background_image.get_width() * 3, self.background_image.get_height() * 2))

    def level_building(self, map_data):
        for row_index, row in enumerate(map_data):
            for col_index, column in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if column == 'X':
                    tile = Tile((x, y), tile_size, 0)
                    self.tiles_sprite_group.add(tile)
                if column == 'B':
                    tile = Tile((x, y), tile_size, 1)
                    self.tiles_sprite_group.add(tile)
                if column == 'P':
                    player_sprite = Player((x, y))
                    self.player.add(player_sprite)
                if column == 'M':
                    money_sprite = Money((x, y))
                    self.money_sprite_group.add(money_sprite)
                    self.money_quantity += 1
                if column == 'L':
                    lava_tile = Tile((x, y), tile_size, 2)
                    self.lava_tiles_group.add(lava_tile)

    def camera_scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < (SCREEN_WIDTH / 4) and direction_x < 0:
            self.map_shift_x = 8
            player.speed_x = 0
        elif player_x > SCREEN_WIDTH - (SCREEN_WIDTH / 4) and direction_x > 0:
            self.map_shift_x = -8
            player.speed_x = 0
        else:
            self.map_shift_x = 0
            player.speed_x = 8
        self.tiles_sprite_group.update(self.map_shift_x, 'x')
        self.lava_tiles_group.update(self.map_shift_x, 'x')
        self.money_sprite_group.update(self.map_shift_x, 'x')

    def camera_scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        if player_y < (SCREEN_HEIGHT / 4) and direction_y < 0:
            self.map_shift_y = 8
            player.speed_y = 0
        elif player_y > SCREEN_HEIGHT - (SCREEN_HEIGHT / 4) and direction_y > 0:
            self.map_shift_y = -8
            player.speed_y = 0
        else:
            self.map_shift_y = 0
            player.speed_y = 8
        self.tiles_sprite_group.update(self.map_shift_y, 'y')
        self.lava_tiles_group.update(self.map_shift_y, 'y')
        self.money_sprite_group.update(self.map_shift_y, 'y')

    def vertical_move(self):
        player = self.player.sprite
        player.rect.y += player.direction.y * player.speed_y
        for sprite in self.tiles_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                elif player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top

    def horizontal_move(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed_x
        for sprite in self.tiles_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left

    def death(self):
        death_flag = False
        player = self.player.sprite
        for sprite in self.lava_tiles_group.sprites():
            if sprite.rect.colliderect(player.rect):
                death_flag = True
        return death_flag

    def get_money(self):
        player = self.player.sprite
        for sprite in self.money_sprite_group.sprites():
            if sprite.rect.colliderect(player.rect):
                self.money_sprite_group.remove(sprite)
                self.money_quantity -= 1
        if self.money_quantity == 0:
            return True

    def run(self):
        self.player.update()
        self.camera_scroll_x()
        self.camera_scroll_y()
        self.background_coordinate_x += self.map_shift_x
        self.background_coordinate_y += self.map_shift_y
        self.display_surface.blit(self.background_image, (self.background_coordinate_x, self.background_coordinate_y))
        self.tiles_sprite_group.draw(self.display_surface)
        self.lava_tiles_group.draw(self.display_surface)
        self.money_sprite_group.draw(self.display_surface)
        self.horizontal_move()
        self.vertical_move()
        self.death()
        self.get_money()
        self.player.draw(self.display_surface)
