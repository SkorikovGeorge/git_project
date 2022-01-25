import pygame
from level_info import SCREEN_WIDTH, SCREEN_HEIGHT


class Result:
    def __init__(self, surface):
        self.display_surface = surface
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image = pygame.image.load('images/space_image/space_background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (
            self.background_image.get_width() * 3, self.background_image.get_height() * 2))

    def run(self):
        self.display_surface.blit(self.background_image, (0, 0))