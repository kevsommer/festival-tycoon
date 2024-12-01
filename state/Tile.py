import random 
import pygame
from core.HexTile import HexTile
from core.AxialHexCoord import AxialHexCoord
from graphics.Camera import Camera
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
        self.color = self.get_color()
        self.text = ""
        
    def __str__(self):
        return f"TileState(id={self.id}, level={self.level}, terrain={self.terrain})"

    def draw(self, screen: pygame.Surface, camera: Camera, selected: bool = False):
        points = list(map(camera.transform_to_screen_coords, self.hex_tile.points))
        pygame.draw.polygon(screen, self.color, points)
        
        if selected:
            width = round(camera.zoom * 5)
            pygame.draw.polygon(screen, COLORS['red'], points, width=width)
            
        fontSize = round(camera.zoom * 16)
        font = pygame.font.Font(None, fontSize)
        text = font.render(self.text, True, COLORS['black'])
        screen_point = camera.transform_to_screen_coords((self.x - 25, self.y))
        screen.blit(text, screen_point)
    

    def get_color(self) -> tuple[int, int, int]:    
        if self.terrain == 'water':
            return COLORS['blue']
        elif self.terrain == 'grass':
            return COLORS['green']
        elif self.terrain == 'mountain':
            return COLORS['gray']
        
        return COLORS['black']
