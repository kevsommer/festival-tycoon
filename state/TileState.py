import random 
from core.HexTile import HexTile
from core.AxialHexCoord import AxialHexCoord

type TileId = tuple[int, int]

random.seed(42)
class TileState:
    def __init__(self, id: TileId, coord: AxialHexCoord):
        self.id = id
        self.level = 0
        self.hex_tile = HexTile(coord)
        self.terrain = random.choice(["grass", "water", "mountain"])
        
    def __str__(self):
        return f"TileState(id={self.id}, level={self.level}, terrain={self.terrain})"

