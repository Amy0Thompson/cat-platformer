import pygame
from pygame.locals import *
pygame.init()
#importing & initializing pygame

screen_width = 500
screen_height = 500
#adding screen dimensions for game

screen = pygame.display.set_mode((screen_height, screen_width))
pygame.display.set_caption('Jump Cat')
#game display + title

background_img = pygame.image.load('bg.png')
scaled_bg = pygame.transform.scale(background_img, (500,500))
dirt_img = pygame.image.load('grassCenter.png')
tile_size = 100 #5x5 grid
scaled_dirt = pygame.transform.scale(dirt_img, (tile_size,tile_size))
#upload & scale game images to fit window


class Map():
    def __init__ (self, data):
        self.tile_list = []
        row_count = 0
        for row in data:
            column_count = 0
            for tile in row: 
                if tile == 1:
                    dirt_rect = scaled_dirt.get_rect() #turns into rectangle
                    dirt_rect.x = column_count * tile_size
                    dirt_rect.y = row_count * tile_size
                    tile = (scaled_dirt, dirt_rect)
                    self.tile_list.append(tile)
                column_count += 1
            row_count += 1
#adds the tiles
    def draw(self): 
            for tile in self.tile_list:
                screen.blit(tile[0], tile[1])    
#displays the tiles
map_data = [
[1, 1, 1, 1, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 0, 0, 0, 1],
[1, 1, 1, 1, 1]
]
map = Map(map_data)
#for creating the map

gameRunning = True
#sets game to running by default
while gameRunning:
#all that happens while game runs is in this while loop
    screen.blit(scaled_bg, (0,0))
    map.draw()
#adds game graphics to display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
#allows user to exit game
    pygame.display.update()
#updates display window w/ the added instructions in code

pygame.quit()