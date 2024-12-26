import pygame
import sys
pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode(width, height) 
pygame.display.set_caption("sunny trail")
backgroundcolor = pygame.image.load("BG1.png")
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() 
            sys.exit()
    screen.blit(backgroundcolor, (0, 0))
    pygame.display.flip()