"""
The main game class making
"""
import pygame

size = width,height = 1280,720

pygame.display.set_caption("Fight")

pygame.init()
screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()

run = True
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        clock.tick(60)
        pygame.display.update()

