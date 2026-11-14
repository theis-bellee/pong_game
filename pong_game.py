import pygame 
import sys

pygame.init()

game_status = "menu"

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("pong_game")

font_title = pygame.font.Font(None, 72)
font_button = pygame.font.Font(None, 36)


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
        
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
    
    
    
    
    pygame.display.flip()


pygame.quit()
sys.exit()