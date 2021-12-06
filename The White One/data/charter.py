import pygame
import The_W_One

##Player Charter

DEFAULT_IMAGE_SIZE = (50,60)


##Player_one

player_one = pygame.image.load('img/characters/forward1.png').convert_alpha()
player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
player_one_rect = player_one.get_rect(midbottom = (60,600))