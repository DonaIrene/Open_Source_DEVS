import pygame
from data.tiles import Tile, Tile2
from data.settings import title_size
from data.charter import Jogador_01

class Level: 
    def __init__(self,level_data,surface):
        ##Level Setup

        self.display_surface = surface
        self.setup_level(level_data)
        self.world_Shift_x = 0
        self.world_Shift_y = 0

    def setup_level (self,layout):
        self.tiles = pygame.sprite.Group()
        self.player_one = pygame.sprite.GroupSingle()

        for row_index,row in enumerate(layout):
            for colun_index,cell in enumerate(row):
                x = colun_index * title_size
                y = row_index * title_size
                
                if cell == 'X':
                    tile = Tile((x,y))
                    self.tiles.add(tile)

                if cell == 'R':
                    tile = Tile2((x,y))
                    self.tiles.add(tile)

                if cell == 'P':
                    player_sprite = Jogador_01((x,y))
                    self.player_one.add(player_sprite)

    def scroll_x (self):
        player = self.player_one.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < 100 and direction_x < 0:
            self.world_Shift_x= 3
            player.speed = 0
        elif player_x > 50 and direction_x > 0:
            self.world_Shift_x =-3
            player.speed = 0
        else:
            self.world_Shift_x = 0
            player.speed = 8

    def scrol_y(self):
        player = self.player_one.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y

        if player_y < 200 and direction_y < 0:
            self.world_Shift_y = 3
            player.speed = 0
        elif player_y > 1000 and direction_y > 0:
            self.world_Shift_y = -3
        else: 
            self.world_Shift_y = 0 
            player.speed = 8
    
    def horizontal_movement_collision (self):
        player = self.player_one.sprite
        player.rect.x = player.direction.x * player.speed

        collide = pygame.Rect.colliderect(self.player_one,self.tiles)
        if collide:
            self.tiles.right = player.left
            


    def run(self):

        #level tiles
        self.tiles.update(self.world_Shift_x,self.world_Shift_y)
        self.tiles.draw(self.display_surface)
        self.scroll_x()
        self.scrol_y()
        
        #Player
        self.player_one.update()
        self.horizontal_movement_collision()
        self.player_one.draw(self.display_surface)

