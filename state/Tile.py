import random 
import pygame
from core.HexTile import HexTile
from core.AxialHexCoord import AxialHexCoord
from assets.colors import COLORS

type TileId = tuple[int, int]

random.seed(42)

class Tile():
    def __init__(self, id: TileId, coord: AxialHexCoord):
        pygame.sprite.Sprite.__init__(self)
        self.x = coord.x
        self.y = coord.y
        self.id = id
        self.level = 0
        self.hex_tile = HexTile(coord)
        self.terrain = random.choice(["grass", "water", "mountain"])
        
    def __str__(self):
        return f"TileState(id={self.id}, level={self.level}, terrain={self.terrain})"

    def draw(self, screen):
        pygame.draw.polygon(screen, COLORS['yellow'], self.hex_tile.points)
