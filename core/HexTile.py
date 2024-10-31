import math

RADIUS = 50
WINDOW_OFFSET_X = 960
WINDOW_OFFSET_Y = 540
class HexTile:
    def __init__(self, x, y):
        self.radius = RADIUS
        self.x = x + WINDOW_OFFSET_X
        self.y = y + WINDOW_OFFSET_Y
        self.points = list(map(lambda i: self.pointy_hex_corner(self.radius, i), range(0, 6)))
        self.lines = zip(self.points[:-1], self.points[1:])

    def pointy_hex_corner(self, size, i):
        angle_deg = 60 * i - 30
        angle_rad = math.pi / 180 * angle_deg

        corner_x = round(self.x + size * math.cos(angle_rad), 2)
        corner_y = round(self.y + size * math.sin(angle_rad), 2)

        return (corner_x, corner_y)
