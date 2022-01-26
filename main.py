import sys
import pygame
from level_info import *
from level import Level
from start_window import Start
import button
from choose_level_window import Choose
from result_window import Result
from game_over import GameOver

pygame.init()
pygame.mixer.music.load('sounds/music.mp3')
pygame.mixer.music.play(-1)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

start = Start(screen)
choose = Choose(screen)
level = Level(level_map, screen)
result = Result(screen)
game_over = GameOver(screen)
go_to_start = True
go_to_choose = False
go_to_level = False
go_to_result = False
go_game_over = False
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
        if level.death():
            go_game_over = True
            timer_stop = True
            go_to_level = False
        if level.get_money():
            while not timer_stop:
                result_time = pygame.time.get_ticks() - start_ticks
                timer_stop = True
            go_to_result = True
            go_to_level = False
    if go_game_over:
        game_over.run()
    if go_to_result:
        result_sound = pygame.mixer.Sound('sounds/result.wav')
        result_sound.play(loops=0)
        result.run()
    clock.tick(FPS)
    pygame.display.update()
