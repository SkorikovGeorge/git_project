import sys
import pygame
from level_info import *
from level import Level
from start_window import Start
import button
from choose_level_window import Choose
from result_window import Result

pygame.init()
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

start = Start(screen)
choose = Choose(screen)
level = Level(level_map, screen)
result = Result(screen)
go_to_start = True
go_to_choose = False
go_to_level = False
go_to_result = False
start_button_image = pygame.image.load('images/button_images/старт.png')
start_button = button.Button(SCREEN_WIDTH // 3.5, SCREEN_HEIGHT // 4, start_button_image, 0.5)
start_button_image2 = pygame.image.load('images/button_images/старт.png')
start_button2 = button.Button(SCREEN_WIDTH // 3, SCREEN_HEIGHT // 2, start_button_image, 0.2)

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if go_to_start:
        start.run()
        if start_button.draw(screen):
            go_to_choose = True
            go_to_start = False
    if go_to_choose:
        choose.run()
        if start_button2.draw(screen):
            go_to_level = True
            go_to_choose = False
            start_ticks = pygame.time.get_ticks()
            timer_stop = False
    if go_to_level:
        level.run()
    if level.get_money():
        while not timer_stop:
            result_time = pygame.time.get_ticks() - start_ticks
            stop = True
        result.run()
        go_to_level = False
    clock.tick(FPS)
    pygame.display.update()
