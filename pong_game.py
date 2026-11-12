import pygame 
import sys

pygame.init()

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("pong_game")

clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)

    
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.display.flip()


pygame.quit()
sys.exit()