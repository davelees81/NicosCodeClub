from ast import Str
from pickle import TRUE


first = input('First : ')
second = input('Second : ')
sum = float(first) + float(second)
print('Sum : ' + str(sum))


import pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

screen = pygame.pygame.display.pygame.display.set_mode((WIDTH, HEIGHT, 0))

game_over is False

while not game_over:
    for event in pygame.event.get:
        if event.type == pygame.QUIT:
            sys.exit()


    pygame.draw.rect(screen, (50, 50, 50), (100, 250, 20, 100))
    pygame.display.update

    game_over is TRUE
game_over is TRUE