
import pygame
from sys import exit

from pygame.constants import KEYDOWN


pygame.init()

screen = pygame.display.set_mode((1220,1030))
clock = pygame.time.Clock()
game_tag = pygame.font.Font('font/breathefire/Breathefire.ttf',20)

map = pygame.Surface((1200,1200))
map.fill('grey12')
game_tag1= game_tag.render('Fire and Water',False,'white')
game_tag2= game_tag.render('Fire and Water',True,'blue1')



##Level maps
map_layer1 = pygame.image.load('img/char select.jpg').convert_alpha()
map_layer1 = pygame.transform.scale(map_layer1,(1200,1100))

mov_down = pygame.K_s

##Players charters
DEFAULT_IMAGE_SIZE = (70,90)

#Mage
mage1= pygame.image.load('img/player/mage.png').convert_alpha()
mage1 = pygame.transform.scale(mage1,DEFAULT_IMAGE_SIZE)
mage_rect = mage1.get_rect(midbottom = (245,250))

#
##Pirate
#pirate = pygame.image.load('img/player/pirate.png').convert_alpha()
#pirate = pygame.transform.scale(pirate,DEFAULT_IMAGE_SIZE)
#pirate_rect = pirate.get_rect(midbottom = (255,890))
#
#
###Defender
#defender1 = pygame.image.load('img/player/defender.png').convert_alpha()
#defender1 = pygame.transform.scale(defender1,DEFAULT_IMAGE_SIZE)
#defender1_rect = defender1.get_rect(midbottom = (960,250))
#
#
##Assassin
#assassin1 = pygame.image.load('img/player/assasin.png').convert_alpha()
#assassin1 = pygame.transform.scale(assassin1,DEFAULT_IMAGE_SIZE)
#assassin1_rect = assassin1.get_rect(midbottom = (1090, 580))
#
##Tank
#tank1 = pygame.image.load('img/player/tank.png').convert_alpha()
#tank1 = pygame.transform.scale(tank1,DEFAULT_IMAGE_SIZE)
#tank1_rect = tank1.get_rect(midbottom = (120,580))
#
##Elf
#elf1 = pygame.image.load('img/player/elf.png').convert_alpha()
#elf1 = pygame.transform.scale(elf1,DEFAULT_IMAGE_SIZE)
#elf1_rect = elf1.get_rect(midbottom = (960,900))
#
##Fary
#fary1 = pygame.image.load('img/player/fary.png').convert_alpha()
#fary1 = pygame.transform.scale(fary1,DEFAULT_IMAGE_SIZE)
#fary1_rect = fary1.get_rect(midbottom = (600,160))


while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               exit()

     screen.blit(map,(10,50))

     #levels
     map.blit(map_layer1,(0,0))

     ##Name Tag
     map.blit(game_tag2,(551,0))
     map.blit(game_tag1,(550,1))
     

     #players locations
     keys = pygame.key.get_pressed()
     if keys[pygame.K_s]:mage_rect.bottom +=5
     if keys[pygame.K_a]:mage_rect.left -= 5
     if keys[pygame.K_w]:mage_rect.top -=5
     if keys[pygame.K_d]:mage_rect.right +=5
     if mage_rect.bottom <=1100 or mage_rect.left >= 1200: mage_rect.bottom = 250
     
     map.blit(mage1,mage_rect)

     

    #pirate_rect.top += 0
    #pirate_rect.bottom -= 0
    #pirate_rect.left -= 0
    #pirate_rect.right += 0
    #if pirate_rect.left <= 0 : pirate_rect.left = 1145
    #map.blit(pirate,pirate_rect)
    #
    #
    #defender1_rect.top += 0
    #defender1_rect.bottom -= 0
    #defender1_rect.left -= 0
    #defender1_rect.right += 0
    #if defender1_rect.bottom <= 0 : defender1_rect.bottom = 963
    #map.blit(defender1,(defender1_rect))

    #assassin1_rect.top += 0
    #assassin1_rect.bottom -= 0
    #assassin1_rect.left -= 0
    #assassin1_rect.right += 0
    #if assassin1_rect.right >=1190 : assassin1_rect.bottom = 963
    #map.blit(assassin1,(assassin1_rect))

    #tank1_rect.top += 0
    #tank1_rect.bottom -= 0
    #tank1_rect.left -= 0
    #tank1_rect.right += 0
    #if tank1_rect.right >=1190 : tank1_rect.bottom = 963
    #map.blit(tank1,(tank1_rect))

    # elf1_rect.top += 0
    # elf1_rect.bottom -= 0
    # elf1_rect.left -= 0
     #elf1_rect.right += 0
    # if elf1_rect.right >=1190 : elf1_rect.bottom = 963
     #map.blit(elf1,(elf1_rect))

     
   #  fary1_rect.top += 0
   #  fary1_rect.bottom -= 0
   #  fary1_rect.left -= 0
   #  fary1_rect.right += 0
    # if fary1_rect.right >=1190 : fary1_rect.bottom = 963
    # map.blit(fary1,(fary1_rect))
     
     ##1v1
    #mouse_pos = pygame.mouse.get_pos()
    #if event.type == pygame.MOUSEMOTION:
    #     print(mouse_pos)
          


     pygame.display.update()
     clock.tick(60)     #FPS