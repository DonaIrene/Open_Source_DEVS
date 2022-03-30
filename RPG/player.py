import pygame
from pygame import key

class Player(pygame.sprite.Sprite):

    def __init__(self,pos):
        super().__init__()
        self.image = pygame.Surface((32,64))
        self.image.fill ('purple')
        self.rect = self.image.get_rect(topleft = pos)
        
        #player moviment
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 1
        self.gravity = 0.8
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            self.direction.x += self.speed
            self.rect.x += self.direction.x

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            self.direction.x -= self.speed
            self.rect.x -= self.direction.x
        
        if keys [pygame.K_w] or keys[pygame.K_UP]:
            self.jump()

    def apply_gravity (self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
        print(self.direction.y)

    def jump(self):
        self.direction.y = self.jump_speed


    def update(self):
        self.get_input()
        self.apply_gravity()
