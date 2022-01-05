import sys
import pygame
from level_info import *
from level import Level

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
level = Level(level_map, screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(BLACK)
    level.run()
    clock.tick(FPS)
    pygame.display.update()

