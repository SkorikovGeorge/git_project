import pygame


class Start:
    def __init__(self, surface):
        self.display_surface = surface
        self.background_coordinate_x = -200
        self.background_coordinate_y = -200
        self.background_image = pygame.image.load('images/space_image/space_background.jpg')
        self.background_image = pygame.transform.scale(self.background_image, (
            self.background_image.get_width() * 2, self.background_image.get_height() * 2))

    def run(self):
        self.display_surface.blit(self.background_image, (self.background_coordinate_x, self.background_coordinate_y))
        pygame.draw.rect(self.display_surface, 'white', pygame.Rect(100, 100, 100, 100))
