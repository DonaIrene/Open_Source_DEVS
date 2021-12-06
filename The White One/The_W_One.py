import pygame
import data.charter
from sys import exit

from pygame import event


pygame.init()

screen = pygame.display.set_mode((1280,720))
clock = pygame.time.Clock()

back_color = pygame.Surface((1280,720))
back_color.fill('black')

lvl1 = pygame.image.load('img/lvl1.jpg').convert()
lvl1 = pygame.transform.scale(lvl1,(1280,720))

##Player Charter

DEFAULT_IMAGE_SIZE = (80,90)


##Player_one

player_one = pygame.image.load('img/charaters/forward1.png').convert_alpha()
player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
player_one_rect = player_one.get_rect(midbottom = (60,600))

while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               exit()

     screen.blit(back_color,(0,0))

     back_color.blit(lvl1,(0,0))

     lvl1.blit(player_one,player_one_rect)

     pygame.display.update()
     clock.tick(60)