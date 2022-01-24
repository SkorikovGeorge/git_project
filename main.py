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
go_to_choose = False
go_to_level = False
go_to_result = False
start_button_image = pygame.image.load('images/button_images/старт.png')
start_button = button.Button(SCREEN_WIDTH // 3.5, SCREEN_HEIGHT // 4, start_button_image, 0.5)

while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    start.run()
    if start_button.draw(screen):
        go_to_level = True
    if go_to_level:
        level.run()
    if level.get_money():
        result.run()
    clock.tick(FPS)
    pygame.display.update()
