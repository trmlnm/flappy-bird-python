import sys
import pygame


pygame.init()


SCREEN_H = 512
SCREEN_W = 288

screen = pygame.display.set_mode((SCREEN_W, SCREEN_H))
clock = pygame.time.Clock()


while True:
    for event in pygame.event.get():

        # enable the quit button on the screen window
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(120)
