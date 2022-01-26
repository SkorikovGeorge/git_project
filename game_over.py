import pygame
from levels_info import SCREEN_WIDTH, SCREEN_HEIGHT


class GameOver:
    def __init__(self, surface):
        self.display_surface = surface
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = pygame.image.load('images/space_image/space_background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (
            self.background_image.get_width() * 3, self.background_image.get_height() * 2))
        font = pygame.font.Font(None, 150)
        self.text = font.render("GAME OVER", True, 'red')
        self.text_w = self.text.get_width()
        self.text_h = self.text.get_height()
        self.text_x = SCREEN_WIDTH // 2 - self.text_w // 2
        self.text_y = SCREEN_HEIGHT // 5

    def run(self):
        self.display_surface.blit(self.background_image, (0, 0))
        self.display_surface.blit(self.text, (self.text_x, self.text_y))
        pygame.draw.rect(self.display_surface, 'red', (self.text_x - 10, self.text_y - 10,
                                                       self.text_w + 20, self.text_h + 20), 1)
