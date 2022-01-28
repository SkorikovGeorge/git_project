import pygame


class Animation(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        frame_1 = pygame.image.load('data/images/start_button_animation/start_button_1.png')
        frame_1 = pygame.transform.scale(frame_1, (frame_1.get_width() * 1.3, frame_1.get_height() * 1.3))
        frame_2 = pygame.image.load('data/images/start_button_animation/start_button_2.png')
        frame_2 = pygame.transform.scale(frame_2, (frame_2.get_width() * 1.3, frame_2.get_height() * 1.3))
        frame_3 = pygame.image.load('data/images/start_button_animation/start_button_3.png')
        frame_3 = pygame.transform.scale(frame_3, (frame_3.get_width() * 1.3, frame_3.get_height() * 1.3))
        frame_4 = pygame.image.load('data/images/start_button_animation/start_button_4.png')
        frame_4 = pygame.transform.scale(frame_4, (frame_4.get_width() * 1.3, frame_4.get_height() * 1.3))
        frame_5 = pygame.image.load('data/images/start_button_animation/start_button_5.png')
        frame_5 = pygame.transform.scale(frame_5, (frame_5.get_width() * 1.3, frame_5.get_height() * 1.3))
        frame_6 = pygame.image.load('data/images/start_button_animation/start_button_6.png')
        frame_6 = pygame.transform.scale(frame_6, (frame_6.get_width() * 1.3, frame_6.get_height() * 1.3))
        frame_7 = pygame.image.load('data/images/start_button_animation/start_button_7.png')
        frame_7 = pygame.transform.scale(frame_7, (frame_7.get_width() * 1.3, frame_7.get_height() * 1.3))
        frame_8 = pygame.image.load('data/images/start_button_animation/start_button_8.png')
        frame_8 = pygame.transform.scale(frame_8, (frame_8.get_width() * 1.3, frame_8.get_height() * 1.3))
        frame_9 = pygame.image.load('data/images/start_button_animation/start_button_9.png')
        frame_9 = pygame.transform.scale(frame_9, (frame_9.get_width() * 1.3, frame_9.get_height() * 1.3))
        frame_10 = pygame.image.load('data/images/start_button_animation/start_button_10.png')
        frame_10 = pygame.transform.scale(frame_10, (frame_10.get_width() * 1.3, frame_10.get_height() * 1.3))
        self.current_frame = 0
        self.frame_sprites = [frame_1, frame_1, frame_1, frame_1, frame_1, frame_1, frame_1, frame_1, frame_1, frame_1,
                              frame_1, frame_2, frame_3, frame_4, frame_5, frame_6, frame_7, frame_8, frame_9, frame_10]
        self.image = self.frame_sprites[self.current_frame]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self, speed):
        self.current_frame += speed
        if self.current_frame >= len(self.frame_sprites):
            self.current_frame = 0
        self.image = self.frame_sprites[int(self.current_frame)]
