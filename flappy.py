import sys
import pygame
import random

# Constants for screen width and height
SCREEN_H = 512
SCREEN_W = 288


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + SCREEN_W, 450))


def create_pipe():
    random_pipe_pos = random.choice(pipe_height)
    bottom_pipe = pipe_surface.get_rect(midtop=(300, random_pipe_pos))
    top_pipe = pipe_surface.get_rect(midbottom=(300, random_pipe_pos - 150))
    return (top_pipe, bottom_pipe)


def move_pipes(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    return pipes


def draw_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom > 512:
            screen.blit(pipe_surface, pipe)
        else:
            flip_pipe = pygame.transform.flip(pipe_surface, False, True)
            screen.blit(flip_pipe, pipe)


pygame.init()

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()

# Game Variables

gravity = 0.125
bird_movement = 0

bg_surface = pygame.image.load('assets/background-day.png').convert()
floor_surface = pygame.image.load('assets/base.png').convert()
floor_x_pos = 0

bird_surface = pygame.image.load('assets/bluebird-midflap.png').convert()
bird_rect = bird_surface.get_rect(center=(50, 256))

pipe_surface = pygame.image.load('assets/pipe-green.png').convert()
pipe_list = []
SPAWNPIPE = pygame.USEREVENT
pygame.time.set_timer(SPAWNPIPE, 1200)
pipe_height = [200, 300, 400]

while True:
    for event in pygame.event.get():

        # enable the quit button on the screen window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # print("flap")
                bird_movement = 0
                bird_movement -= 6

        if event.type == SPAWNPIPE:
            # print("pipe")
            pipe_list.extend(create_pipe())

    screen.blit(bg_surface, (0, 0))

    # Bird
    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)

    # Pipes
    pipe_list = move_pipes(pipe_list)
    draw_pipes(pipe_list)

    # Floor
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -SCREEN_W:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
