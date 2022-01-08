import sys
import pygame
from level_info import *
from level import Level
from start_window import Start

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60
start = Start(screen)
level = Level(level_map, screen)
go_to_level = False


while True:
    screen.fill(BLACK)
    start.run()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN or event.type == pygame.MOUSEBUTTONUP:
            x, y = event.pos
            print(x, y)
            if 100 <= x <= 200 and 100 <= y <= 200:
                print('yes')
                go_to_level = True
    if go_to_level:
        level.run()
    clock.tick(FPS)
    pygame.display.update()
