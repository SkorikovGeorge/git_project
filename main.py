import sys
import pygame
from levels_info import *
from level_1 import *
from level_2 import *
from score import *
from level import Level
from start_window import Start
from choose_level_window import Choose
from result_window import Result
from game_over import GameOver
from animation import *

pygame.init()
pygame.mixer.music.load('data/sounds/music.mp3')
pygame.mixer.music.play(-1)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()
FPS = 60

start = Start(screen)
choose = Choose(screen)
level_1 = Level(level_1_map, screen)
level_2 = Level(level_2_map, screen)
result = Result(screen)
game_over = GameOver(screen)

go_to_start = True
go_to_choose = False
go_to_level_1 = False
go_to_level_2 = False
go_to_level_3 = False
go_to_result = False
go_game_over = False

moving_sprites = pygame.sprite.Group()
animation = Animation(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)
moving_sprites.add(animation)


while True:
    screen.fill(BLACK)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if go_to_start:
        start.run()
        if start.button():
            go_to_choose = True
            go_to_start = False
        moving_sprites.draw(screen)
        moving_sprites.update(0.6)
    if go_to_choose:
        choose.run()
        if choose.button() == 1:
            pygame.mixer.music.pause()
        elif choose.button() == 2:
            pygame.mixer.music.unpause()
        elif choose.button() == 0:
            go_to_level_1 = True
            go_to_choose = False
            start_ticks = pygame.time.get_ticks()
            timer_stop = False
        elif choose.button() == 3:
            go_to_level_2 = True
            go_to_choose = False
            start_ticks = pygame.time.get_ticks()
            timer_stop = False
        elif choose.button() == 4:
            go_to_start = True
            go_to_choose = False
    if go_to_level_1:
        level_1.run()
        if level_1.death():
            level_1.again(level_1_map, screen)
            go_game_over = True
            start_ticks = 0
            go_to_level_1 = False
        if level_1.get_money():
            while not timer_stop:
                result_time = pygame.time.get_ticks() - start_ticks
                new_score = score(result_time)
                current_best_time = get_best_result('data/levels_score/level_1_score.txt')
                current_best_score = score(current_best_time)
                if result_time < int(current_best_time):
                    write_new_best_result('data/levels_score/level_1_score.txt', str(result_time))
                start_ticks = 0
                timer_stop = True
            level_1.again(level_1_map, screen)
            go_to_result = True
            go_to_level_1 = False
    if go_to_level_2:
        level_2.run()
        if level_2.death():
            level_2.again(level_2_map, screen)
            go_game_over = True
            start_ticks = 0
            go_to_level_2 = False
        if level_2.get_money():
            while not timer_stop:
                result_time = pygame.time.get_ticks() - start_ticks
                new_score = score(result_time)
                current_best_time = get_best_result('data/levels_score/level_2_score.txt')
                current_best_score = score(current_best_time)
                if result_time < int(current_best_time):
                    write_new_best_result('data/levels_score/level_2_score.txt', str(result_time))
                start_ticks = 0
                timer_stop = True
            level_2.again(level_2_map, screen)
            go_to_result = True
            go_to_level_2 = False
    if go_game_over:
        game_over.run()
        if game_over.button():
            go_to_choose = True
            go_game_over = False
    if go_to_result:
        result.run(new_score, current_best_score, result_time, int(current_best_time))
        if result.button():
            go_to_choose = True
            go_to_result = False
    clock.tick(FPS)
    pygame.display.update()
