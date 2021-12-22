import pygame
from tiles import Tile
from settings import title_size


class Level: 
    def __init__(self,level_data,surface):
        ##Level Setup

        self.display_surface = surface
        self.setup_level(level_data)
        self.world_Shift = -4

    def setup_level (self,layout):
        self.tiles = pygame.sprite.Group()
        for row_index,row in enumerate(layout):
            for colun_index,cell in enumerate(row):
                if cell == 'X':
                    x = colun_index * title_size
                    y = row_index * title_size
                    tile = Tile((x,y),title_size)
                    self.tiles.add(tile)

    def run(self):
        self.tiles.update(-4)
        self.tiles.draw(self.display_surface)
        