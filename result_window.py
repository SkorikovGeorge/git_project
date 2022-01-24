import pygame
from level_info import SCREEN_WIDTH, SCREEN_HEIGHT


class Result:
    def __init__(self, surface):
        self.display_surface = surface
        self.background_image = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.background_image.fill('orange')

    def run(self):
        self.display_surface.blit(self.background_image, (0, 0))