import pygame

class Titles(pygame.sprite.Sprite):
    def __init__(self,pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('grey')
        self.rect = self.imgage.get_rect(topleft = pos)