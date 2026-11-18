import pygame 
import sys

pygame.init()

game_status = "menu"

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("pong_game")

font_title = pygame.font.Font(None, 72)
font_button = pygame.font.Font(None, 36)


class Button:
    def __init__(self, text, rx, ry, action, rwidth, rheight, font, color_darck):
        self.text = text 
        self.action = action
        self.rx = rx          
        self.ry = ry
        self.rwidth = rwidth
        self.rheight = rheight
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.font = font
        self.color_drack = color_darck
        self.color_light = tuple(min(c + 60, 255) for c in self.color_darck)
    
    def update_rect(self, win_width, win_height):
        text_width, text_height = self.font.size(self.text)
        
        padding = 20
        w = int(text_width + padding)
        h = int(text_height + padding)
        x = int(self.rx * win_width)
        y = int(self.ry * win_height)
        
        self.rect = pygame.Rect(0, 0, w, h)
        self.rect.center = (x, y)
    
    def draw(self, win, win_width, win_height, mouse_pos):
        self.update_rect(win_width, win_height)

        if self.rect.collidepoint(mouse_pos):
            current_color = self.color_light
        else:
            current_color = self.color_drack
            
        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, current_color, (0, 0, self.rect.width, self.rect.height), border_radius = 16)
        win.blit(button_surface, self.rect.topleft)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        win.blit(text_surf, text_rect)

    def is_cliked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]
    
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