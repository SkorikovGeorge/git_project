import pygame
from levels_info import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button
from score import *


class Choose:
    def __init__(self, surface):
        self.display_surface = surface
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 75))
        self.show_level_1_score = False
        self.show_level_2_score = False
        back_button_image = pygame.image.load('data/images/button_images/back button.png')
        self.back_on_start_window_button = Button(SCREEN_WIDTH * 0.91, SCREEN_HEIGHT * 0.9, back_button_image, 0.9)
        best_score_image = pygame.image.load('data/images/button_images/cup button.png')
        self.level_1_best_score_button = Button(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.33, best_score_image, 0.185)
        self.level_2_best_score_button = Button(SCREEN_WIDTH * 0.33, SCREEN_HEIGHT * 0.66, best_score_image, 0.185)
        level_1_button_image = pygame.image.load('data/images/button_images/level 1 button.png')
        level_2_button_image = pygame.image.load('data/images/button_images/level 2 button.png')
        self.level_1_button = Button(SCREEN_WIDTH // 6, SCREEN_HEIGHT * 0.33, level_1_button_image, 1)
        self.level_2_button = Button(SCREEN_WIDTH // 6, SCREEN_HEIGHT * 0.66, level_2_button_image, 1)
        music_button_image = pygame.image.load('data/images/button_images/mute_button.png')
        self.music_button = Button(SCREEN_WIDTH * 0.94, SCREEN_HEIGHT * 0.1, music_button_image, 0.2)
        self.music_click_count = 0
        self.result = -1
        self.font = pygame.font.Font('data/letters.ttf', 20)
        self.text1 = self.font.render('Rules of the game:', True, 'yellow')
        self.text2 = self.font.render('collect the trash quickly,', True, 'yellow')
        self.text3 = self.font.render('but avoid lava meteorites - they will kill you.', True, 'yellow')
        self.text4 = self.font.render('Good luck!', True, 'yellow')
        self.text_w1 = self.text1.get_width()
        self.text_w2 = self.text2.get_width()
        self.text_w3 = self.text3.get_width()
        self.text_w4 = self.text4.get_width()
        self.text_h = self.text1.get_height()
        self.text_x = 550
        self.text_y1 = 180
        self.text_y2 = 200 + self.text_h + 30
        self.text_y3 = 200 + self.text_h * 2 + 60
        self.text_y4 = 200 + self.text_h * 3 + 90

    def button(self):
        return self.result

    def run(self):
        level_1_score_text = self.font.render(f'YOUR BEST: {score(get_best_result("data/levels_score/level_1_score.txt"))}', False,
                                              'white')
        level_2_score_text = self.font.render(f'YOUR BEST: {score(get_best_result("data/levels_score/level_2_score.txt"))}', False,
                                              'white')
        self.display_surface.blit(self.background, (0, 0))
        self.display_surface.blit(self.text1, (self.text_x, self.text_y1))
        pygame.draw.rect(self.display_surface, 'yellow', (self.text_x - 10, self.text_y1 - 10,
                                                          self.text_w1 + 20, self.text_h + 20), 1)
        self.display_surface.blit(self.text2, (self.text_x, self.text_y2))
        self.display_surface.blit(self.text3, (self.text_x, self.text_y3))
        self.display_surface.blit(self.text4, (self.text_x, self.text_y4))
        if self.level_1_best_score_button.draw(self.display_surface):
            self.show_level_1_score = True
        if self.show_level_1_score:
            self.display_surface.blit(level_1_score_text, (SCREEN_WIDTH * 0.27, SCREEN_HEIGHT * 0.42))
        if self.level_2_best_score_button.draw(self.display_surface):
            self.show_level_2_score = True
        if self.show_level_2_score:
            self.display_surface.blit(level_2_score_text, (SCREEN_WIDTH * 0.27, SCREEN_HEIGHT * 0.75))
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
