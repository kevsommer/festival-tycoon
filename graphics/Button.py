import pygame
from assets.colors import COLORS

class Button:
    def __init__(self, x: int, y: int):
        self.width: int = 100
        self.height: int = 50
        self.x: int = x
        self.y: int = y
        self.rect: pygame.Rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.color: tuple[int, int, int] = COLORS['white']
        self.text: str = "Button"
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(self.text, True, COLORS['black'])
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)
        
    def draw(self, screen: pygame.Surface):
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text_surface, self.text_rect)
        
    def hover(self, mouse_pos: tuple[int, int]) -> bool:
        if (self.rect.collidepoint(mouse_pos)):
            self.color = COLORS['light_gray']
            return True
        else:
            self.color = COLORS['white']
            return False
