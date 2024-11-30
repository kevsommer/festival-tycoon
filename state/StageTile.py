from .Tile import Tile

class StageTile(Tile):
    def __init__(self, id, coord):
        super().__init__(id, coord)
        self.level = 1
    
    def __str__(self):
        return f"StageTile(id={self.id}, level={self.level}, terrain={self.terrain})"
