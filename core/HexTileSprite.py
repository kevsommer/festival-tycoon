from .HexTile import HexTile
import pygame
import random

class HexTileSprite(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.hex_tile = HexTile(x, y)
        self.color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    def draw_hexagon(self, Surface):
        pygame.draw.polygon(Surface, self.color, self.hex_tile.points)
        pygame.draw.lines(Surface, (0, 0, 0), True, self.hex_tile.points, 5)

    def draw(self, screen):
        self.draw_hexagon(screen)
