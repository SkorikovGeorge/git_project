import pygame
from levels_info import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button


class Choose:
    def __init__(self, surface):
        self.display_surface = surface
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 75))
        back_button_image = pygame.image.load('images/button_images/back button.png')
        self.back_on_start_window_button = Button(SCREEN_WIDTH * 0.91, SCREEN_HEIGHT * 0.9, back_button_image, 0.9)
        best_score_image = pygame.image.load('images/button_images/cup button.png')
        self.level_1_best_score_button = Button(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.33, best_score_image, 0.185)
        self.level_2_best_score_button = Button(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.66, best_score_image, 0.185)
        level_1_button_image = pygame.image.load('images/button_images/level 1 button.png')
        level_2_button_image = pygame.image.load('images/button_images/level 2 button.png')
        self.level_1_button = Button(SCREEN_WIDTH // 6, SCREEN_HEIGHT * 0.33, level_1_button_image, 1)
        self.level_2_button = Button(SCREEN_WIDTH // 6, SCREEN_HEIGHT * 0.66, level_2_button_image, 1)
        music_button_image = pygame.image.load('images/button_images/mute_button.png')
        self.music_button = Button(SCREEN_WIDTH * 0.94, SCREEN_HEIGHT * 0.1, music_button_image, 0.2)
        self.music_click_count = 0
        self.result = -1

    def button(self):
        return self.result

    def run(self):
        self.display_surface.blit(self.background, (0, 0))
        self.level_1_best_score_button.draw(self.display_surface)
        self.level_2_best_score_button.draw(self.display_surface)
        if self.level_1_button.draw(self.display_surface):
            self.result = 0
        elif self.level_2_button.draw(self.display_surface):
            self.result = 3
        elif self.back_on_start_window_button.draw(self.display_surface):
            self.result = 4
        elif self.music_button.draw(self.display_surface):
            self.music_click_count += 1
            if self.music_click_count % 2 == 1:
                self.result = 1
            else:
                self.result = 2
        else:
            self.result = -1
