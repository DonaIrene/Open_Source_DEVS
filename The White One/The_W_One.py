
import pygame
import data.charter
from sys import exit

from pygame import event
from data.level import Level
from data.settings import level_map,screen_width,screen_heigth


pygame.init()

screen = pygame.display.set_mode((screen_width, screen_heigth))
clock = pygame.time.Clock()
level = Level(level_map,screen)

back_color = pygame.Surface((1920,1020))
back_color.fill("black")

lvl1 = pygame.image.load('img/lvl1.jpg').convert_alpha()
lvl1 = pygame.transform.scale(lvl1,(1920,1020))

##Player Charter

DEFAULT_IMAGE_SIZE = (80,90)

##Player_one
#keys = pygame.key.get_pressed()...
#
#if keys[pygame.KEYDOWN] and [pygame.K_d]:
#     player_one = pygame.image.load('img/characters/foward.png').convert_alpha()
#     player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
#     player_one_rect = player_one.get_rect(midbottom = (60,600))
#
#else:
#     player_one = pygame.image.load('img/charaters/forward1.png').convert_alpha()
#     player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
#     player_one_rect = player_one.get_rect(midbottom = (60,600))


while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               exit()


     screen.fill('black')
     screen.blit(lvl1,(0,-150))
     lvl1.blit(lvl1,(0,0))

     #lvl1.blit(player_one,player_one_rect)
     level.run()
     pygame.display.update()
     clock.tick(30)