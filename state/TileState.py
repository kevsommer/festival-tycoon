import random 

type TileId = tuple[int, int]

random.seed(42)
class TileState:
    def __init__(self, id: TileId):
        self.id = id
        self.level = 0
        self.terrain = random.choice(["grass", "water", "mountain"])
        
    def __str__(self):
        return f"TileState(id={self.id}, level={self.level}, terrain={self.terrain})"

