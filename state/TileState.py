import random 

type TileId = tuple[int, int]

class TileState:
    def __init__(self, id: tuple[int, int]):
        self.id = id
        self.terrain = random.choice(["grass", "water", "mountain"])
