import pygame
from level_info import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button


class Choose:
    def __init__(self, surface):
        self.display_surface = surface
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = pygame.image.load('images/space_image/space_background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (
            self.background_image.get_width() * 3, self.background_image.get_height() * 2))
        choose_button_image = pygame.image.load('images/button_images/старт.png')
        self.choose_button = Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, choose_button_image, 0.2)
        music_button_image = pygame.image.load('images/button_images/старт.png')
        self.music_button = Button(SCREEN_WIDTH // 5, SCREEN_HEIGHT // 5, music_button_image, 0.2)
        self.music_click_count = 0
        self.result = -1

    def button(self):
        return self.result

    def run(self):
        self.display_surface.blit(self.background_image, (0, 0))
        if self.choose_button.draw(self.display_surface):
            self.result = 0
        elif self.music_button.draw(self.display_surface):
            self.music_click_count += 1
            if self.music_click_count % 2 == 1:
                self.result = 1
            else:
                self.result = 2
