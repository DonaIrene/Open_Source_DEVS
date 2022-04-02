import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('The White One/img/unknown.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,30))
        self.image.blit(self.image,(0,0))
        self.rect = self.image.get_rect(midbottom = pos)
    def update(self,x_Shift,y_shift):
        self.rect.x += x_Shift
        self.rect.y += y_shift
        
class Tile2(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('The White One/img/unknown3.png').convert_alpha()
        self.image = pygame.transform.scale(self.image,(30,30))
        self.image.blit(self.image,(0,0))
        self.rect = self.image.get_rect(midbottom = pos)

    def update(self,x_Shift,y_shift):
        self.rect.x += x_Shift
        self.rect.y += y_shift