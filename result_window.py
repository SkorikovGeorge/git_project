import pygame
from levels_info import SCREEN_WIDTH, SCREEN_HEIGHT
from button import Button


class Result:
    def __init__(self, surface):
        self.display_surface = surface
        self.background = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background.fill((0, 0, 75))

        self.font = pygame.font.Font('letters.ttf', 50)
        self.font1 = pygame.font.Font('letters.ttf', 100)
        self.text = self.font.render("RESULTS", True, 'yellow')
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.text_x = SCREEN_WIDTH // 2 - self.text_w // 2
        self.text_y = SCREEN_HEIGHT // 5

        back_button_image = pygame.image.load('images/button_images/back button.png')
        self.back_on_start_window_button = Button(SCREEN_WIDTH * 0.09, SCREEN_HEIGHT * 0.9, back_button_image, 0.9)

    def button(self):
        if self.back_on_start_window_button.draw(self.display_surface):
            return True

    def run(self, result, record, int_result, int_record):
        self.display_surface.blit(self.background, (0, 0))

        self.display_surface.blit(self.text, (self.text_x, self.text_y))
        pygame.draw.rect(self.display_surface, 'yellow', (self.text_x - 10, self.text_y - 10,
                                                          self.text_w + 20, self.text_h + 20), 1)

        self.text1 = self.font.render("Your time  " + result, True, 'yellow')
        self.text_w1 = self.text1.get_width()
        self.text_h1 = self.text1.get_height()
        self.text_x1 = SCREEN_WIDTH // 2 - self.text_w1 // 2
        self.text_y1 = self.text_y + self.text_h1 + 20
        self.display_surface.blit(self.text1, (self.text_x1, self.text_y1))

        self.text2 = self.font.render("Record time  " + record, True, 'yellow')
        self.text_w2 = self.text2.get_width()
        self.text_h2 = self.text2.get_height()
        self.text_x2 = SCREEN_WIDTH // 2 - self.text_w2 // 2
        self.text_y2 = self.text_y1 + self.text_h2 + 20
        self.display_surface.blit(self.text2, (self.text_x2, self.text_y2))

        if int_result < int_record:
            self.text3 = self.font1.render("NEW RECORD!", True, 'red')
            self.text_w3 = self.text3.get_width()
            self.text_h3 = self.text3.get_height()
            self.text_x3 = SCREEN_WIDTH // 2 - self.text_w3 // 2
            self.text_y3 = self.text_y2 + 40
            self.display_surface.blit(self.text3, (self.text_x3, self.text_y3))

