import math
from .AxialHexCoord import AxialHexCoord

RADIUS = 50

class HexTile:
    def __init__(self, coord: AxialHexCoord):
        self.radius = RADIUS
        self.x = coord.x
        self.y = coord.y
        self.points = list(map(lambda i: self.pointy_hex_corner(self.radius, i), range(0, 6)))
        self.lines = zip(self.points[:-1], self.points[1:])

    def pointy_hex_corner(self, size, i):
        angle_deg = 60 * i - 30
        angle_rad = math.pi / 180 * angle_deg

        corner_x = round(self.x + size * math.cos(angle_rad), 2)
        corner_y = round(self.y + size * math.sin(angle_rad), 2)

        return (corner_x, corner_y)
