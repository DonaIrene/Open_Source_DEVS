import pygame,sys
from player import Player

# Game data
from settings import *
from tiles import Tile
from level import Level


# Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_heigth))
clock = pygame.time.Clock()
level = Level(level_map,screen)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)