import pygame
import time
from pygame.locals import * 

pygame.init()

WIDTH = 600
HEIGHT = 600

screen = pygame.display.set_mode((WIDTH, HEIGHT))

object_x = 200
object_y = 200
rocket = pygame.image.load('Space_Rocket/Rocket.png')
space = pygame.image.load('Space_Rocket/Space.png')

run = True 
keys = [False, False, False, False]

while object_y < 600:
    screen.blit(space, (0,0))
    screen.blit(rocket, (object_x,object_y))
    pygame.display.update()

    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False
        
        if i.type == pygame.KEYDOWN:
            if i.key == K_UP:
                keys [0] = True
            elif i.key == K_DOWN:
                keys [1] = True
            elif i.key == K_LEFT:
                keys [2] = True
            elif i.key == K_RIGHT:
                keys [3] = True 

        if i.type == pygame.KEYUP:
            if i.key == K_UP:
                keys [0] = False
            elif i.key == K_DOWN:
                keys [1] = False
            elif i.key == K_LEFT:
                keys [2] = False
            elif i.key == K_RIGHT:
                keys [3] = False

    if keys [0]:
        if object_y > 0:
            object_y = object_y - 2
    if keys [1]:
        if object_y < 600:
            object_y += 2
    if keys [2]:
        if object_x > 0: 
            object_x -= 2
    if keys [3]:
        if object_x < 500:
            object_x += 2

    object_y = object_y + 1

print('Game Over')