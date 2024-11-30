from .Tile import Tile
from assets.colors import COLORS

class StageTile(Tile):
    def __init__(self, id, coord):
        super().__init__(id, coord)
        self.level = 1
        self.color = COLORS['yellow']

    def __str__(self):
        return f"StageTile(id={self.id}, level={self.level}, terrain={self.terrain})"
