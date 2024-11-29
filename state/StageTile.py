from .TileState import TileState

class StageTile(TileState):
    def __init__(self, id):
        super().__init__(id)
        self.level = 1
    
    def __str__(self):
        return f"StageTile(id={self.id}, level={self.level}, terrain={self.terrain})"
