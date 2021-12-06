
import pygame
from sys import exit


pygame.init()

screen = pygame.display.set_mode((1240,1050))
clock = pygame.time.Clock()
game_tag = pygame.font.Font('Dungeons/font/breathefire/Breathefire.ttf',50)

map = pygame.Surface((1220,1030))
map.fill('grey12')
game_tag1= game_tag.render('Fire and Water',False,'grey12')


##Level maps
map_layer1 = pygame.image.load('Dungeons/img/clue mapp.jpg').convert()
map_layer1 = pygame.transform.scale(map_layer1,(1200,1010))


##Players charters
DEFAULT_IMAGE_SIZE = (50,60)

#Mage
mage1= pygame.image.load('Dungeons/img/player/mage.png').convert_alpha()
mage1 = pygame.transform.scale(mage1,DEFAULT_IMAGE_SIZE)
mage_rect = mage1.get_rect(midbottom = (495,85))
mage_x_pos  = 0
mage_y_pos = 0

#Pirate
pirate = pygame.image.load('Dungeons/img/player/pirate.png').convert_alpha()
pirate = pygame.transform.scale(pirate,DEFAULT_IMAGE_SIZE)
pirate_rect = pirate.get_rect(midbottom = (1145,795))
pirate_x_pos = 0
pirate_y_pos = 0

##Defender
defender1 = pygame.image.load('Dungeons/img/player/defender.png').convert_alpha()
defender1 = pygame.transform.scale(defender1,DEFAULT_IMAGE_SIZE)
defender1_rect = defender1.get_rect(midbottom = (405,980))
defende_x_pos = 0
defende_y_pos = 0




while True:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               pygame.quit()
               exit()

     screen.blit(map,(10,10))

     #levels
     map.blit(map_layer1,(10,10))

     ##Name Tag
     map.blit(game_tag1,(500,0))

     #players locations
     
     
     mage_rect.bottom +=1
     if mage_rect.bottom <=0 : mage_rect = 495
     map.blit(mage1,mage_rect)

     
     pirate_rect.left -= 1
     if pirate_rect.bottom <= 0 : pirate_rect.bottom = 790
     map.blit(pirate,pirate_rect)
     
     
     defender1_rect.bottom -= 1
     map.blit(defender1,(defender1_rect))


     pygame.display.update()
     clock.tick(60)     #FPS