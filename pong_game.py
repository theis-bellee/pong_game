import pygame 
import sys

pygame.init()

game_status = "menu"

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("pong_game")


class Boutton:
    def __init__(self, ):
        pass

    
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