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
#upload & scale game background image to fit window

gameRunning = True
#sets game to running by default
while gameRunning:
#all that happens while game runs is in this while loop
    screen.blit(scaled_bg, (0,0))
#adds background image to display
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
#allows user to exit game
    pygame.display.update()
#updates display window w/ the added instructions in code

pygame.quit()