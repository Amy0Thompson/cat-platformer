import pygame
from pygame.locals import *
pygame.init()
#importing & initializing pygame

screen_width = 500
screen_height = 500
#adding screen dimensions for game

screen = pygame.display.set_mode(screen_height, screen_width)
pygame.display.set_caption('Jump Cat')
#game display + title

gameRunning = True
while gameRunning:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameRunning = False
#allows user to exit game

pygame.quit()