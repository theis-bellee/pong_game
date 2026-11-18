import pygame 
import sys

pygame.init()

game_status = "menu"

window = pygame.display.set_mode((800, 600), pygame.RESIZABLE)
pygame.display.set_caption("pong_game")

font_title = pygame.font.Font(None, 72)
font_button = pygame.font.Font(None, 36)

background_menu = pygame.transform.scale(pygame.image.load("pong_game/assets/menu_background.png"), (800, 600))


class Button:
    def __init__(self, text, rx, ry, action, font, color_dark):
        self.text = text 
        self.action = action
        self.rx = rx          
        self.ry = ry
        self.rect = pygame.Rect(0, 0, 0, 0)
        self.font = font
        self.color_dark = color_dark
        self.color_light = tuple(min(c + 60, 255) for c in self.color_dark)
    
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
            current_color = self.color_dark

        button_surface = pygame.Surface((self.rect.width, self.rect.height), pygame.SRCALPHA)
        pygame.draw.rect(button_surface, current_color, (0, 0, self.rect.width, self.rect.height), border_radius = 16)
        win.blit(button_surface, self.rect.topleft)

        text_surf = self.font.render(self.text, True, (255, 255, 255))
        text_rect = text_surf.get_rect(center=self.rect.center)
        win.blit(text_surf, text_rect)

    def is_cliked(self, mouse_pos, mouse_pressed):
        return self.rect.collidepoint(mouse_pos) and mouse_pressed[0]

play_button = Button(text="Jouer", rx=0.5, ry=0.5, action="game", font=font_button, color_dark=(0, 0, 0))    
clock = pygame.time.Clock()
running = True

while running:
    clock.tick(60)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        elif event.type == pygame.VIDEORESIZE:
            window = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            background_menu = pygame.transform.scale(pygame.image.load("pong_game/assets/menu_background.png"), (event.w, event.h))

        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()
            if play_button.is_cliked(mouse_pos, mouse_pressed):
                game_status = play_button.action

    win_w, win_h = window.get_size()
    window.fill((0, 0, 0))  

    if game_status == 'menu':

        window.blit(background_menu, (0, 0))

        title_surf = font_title.render("pong game", True, (255, 255, 255))
        title_rect = title_surf.get_rect()
        title_rect.centerx = win_w // 2
        title_rect.top = int(win_h * 0.07)
        window.blit(title_surf, title_rect)
        
        play_button.draw(window, window.get_width(), window.get_height(), pygame.mouse.get_pos())

    
    
    
    pygame.display.flip()


pygame.quit()
sys.exit()