import pygame
from sys import *

pygame.init()
pygame.display.init()

screen = pygame.display.set_mode((600,600))
pygame.display.set_caption('branching')

clock = pygame.time.Clock()
run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
    screen.fill((100,101,109))
    pygame.draw.rect(screen,"red",(0,0,100,100),0)
    pygame.display.update()
    clock.tick(60)