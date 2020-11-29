import sys
import pygame

# Constants for screen width and height
SCREEN_H = 512
SCREEN_W = 288


def draw_floor():
    screen.blit(floor_surface, (floor_x_pos, 450))
    screen.blit(floor_surface, (floor_x_pos + SCREEN_W, 450))


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

while True:
    for event in pygame.event.get():

        # enable the quit button on the screen window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print("flap")
                bird_movement = 0
                bird_movement -= 6

    screen.blit(bg_surface, (0, 0))

    bird_movement += gravity
    bird_rect.centery += bird_movement
    screen.blit(bird_surface, bird_rect)
    floor_x_pos -= 1
    draw_floor()
    if floor_x_pos <= -SCREEN_W:
        floor_x_pos = 0

    pygame.display.update()
    clock.tick(120)
