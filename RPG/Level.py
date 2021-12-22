import pygame
from Titles import Titles


class Level: 
    def __init__(self,level_data,surface):
        self.display_surface = surface
        self.level_data = level_data

    def setup_level (self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for colun_index,cell in enumerate(row):
                print(f'{row_index},{colun_index}:{cell}')
        

    def run(self):
        self.tiles.draw(self.display_surface)
        