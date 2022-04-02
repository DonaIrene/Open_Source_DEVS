
import pygame

from pygame import key

##Player Charter

DEFAULT_IMAGE_SIZE = (50,60)


##Player_one

class Jogador_01(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 0.1
        self.gravity = 0.08
        self.jump_speed = 0.3
        self.image = pygame.image.load('The White One/img/charaters/forward.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,DEFAULT_IMAGE_SIZE)
        self.rect = self.image.get_rect(midbottom = pos)

    def foward(self):
        self.direction.x += self.speed
        self.rect.x += self.direction.x
        print(self.direction.x)

    def backward(self):
        self.direction.x -= self.speed
        self.rect.x -= self.direction.x
        print(self.direction.x)

    def jump_up(self):
        self.direction.y += self.jump_speed
        self.rect.y += self.direction.y   
        print(self.direction.y)

    def crouch(self):
        self.direction.y += self.speed
        self.rect.y -= self.direction.y
        print(self.direction.y)

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        print(self.direction.y)

    def get_input(self):
        keys = key.get_pressed()
        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            #self.foward() 
            self.direction.x += 1
            self.rect.x += self.direction.x
            print(self.direction.x)
        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            #self.backward()
            self.direction.x -= 1
            self.rect.x -= self.direction.x
            print(self.direction.x)
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            #self.jump_up()
            self.direction.y -= self.jump_speed
            self.rect.y += self.direction.y
            print(self.direction.y)
        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            #self.crouch()
            self.direction.y += 1
            self.rect.y -= self.direction.y
            print(self.direction.y)
    
    def update(self,x_Shift,y_shift):
        self.rect.x += x_Shift
        self.rect.y += y_shift

    def update(self):
        self.get_input()
        self.apply_gravity()
        
    




#keys = pygame.key.get_pressed()

#if keys[pygame.KEYDOWN] and [pygame.K_d]:
#     player_one = pygame.image.load('img/characters/foward.png').convert_alpha()
#     player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
#     player_one_rect = player_one.get_rect(midbottom = (60,600))
#
#else:
#     player_one = pygame.image.load('img/charaters/forward1.png').convert_alpha()
#     player_one = pygame.transform.scale(player_one,DEFAULT_IMAGE_SIZE)
#     player_one_rect = player_one.get_rect(midbottom = (60,600))
