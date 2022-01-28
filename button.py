import pygame


class Button:
    def __init__(self, x, y, image, scale):
        width = image.get_width()
        height = image.get_height()
        self.image = pygame.transform.scale(image, (width * scale, height * scale))
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.clicked = False

    def draw(self, surface):
        # прорисовка кнопки
        surface.blit(self.image, (self.rect.x, self.rect.y))
        pos = pygame.mouse.get_pos()
        action = False

        # отработка нажатия кнопки
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked is False:
                self.clicked = True
                action = True
        if pygame.mouse.get_pressed()[0] == 0:
            self.clicked = False
        return action
