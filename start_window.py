import pygame
from levels_info import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button


class Start:
    def __init__(self, surface):
        self.display_surface = surface
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 75))
        font = pygame.font.Font('data/letters.ttf', 50)
        self.text = font.render("TEXT", True, 'yellow')
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.text_x = SCREEN_WIDTH // 2 - self.text_w // 2
        self.text_y = SCREEN_HEIGHT // 5
        start_button_image = pygame.image.load('data/images/button_images/start button.png')
        self.start_button = Button(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, start_button_image, 1.25)

    def button(self):
        if self.start_button.draw(self.display_surface):
            return True

    def run(self):
        self.display_surface.blit(self.background, (0, 0))
        self.display_surface.blit(self.text, (self.text_x, self.text_y))
        pygame.draw.rect(self.display_surface, 'yellow', (self.text_x - 10, self.text_y - 10,
                                                          self.text_w + 20, self.text_h + 20), 1)
