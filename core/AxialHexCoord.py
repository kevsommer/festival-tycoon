import math

class AxialHexCoord:
    def __init__(self, q, r):
        self.radius = 50
        self.q = q
        self.r = r

        self.x = self.radius * (math.sqrt(3) * self.q  +  math.sqrt(3)/2 * self.r)
        self.y = self.radius * (3/2 * self.r)
        self.pos = (self.x, self.y)
