import math

RADIUS = 50

class AxialHexCoord:
    def __init__(self, q, r):
        self.radius = RADIUS
        self.q = q
        self.r = r

        self.x = self.radius * (math.sqrt(3) * self.q  +  math.sqrt(3)/2 * self.r)
        self.y = self.radius * (3/2 * self.r)
        self.pos = (self.x, self.y)

    @staticmethod
    def pixel_to_hex(point: tuple[int, int]) -> tuple[int, int]:
        x, y = point
        q_frac = math.sqrt(3)/3 * x / RADIUS - 1/3 * y / RADIUS
        r_frac = 2/3 * y / RADIUS

        return AxialHexCoord.axial_round((q_frac, r_frac))
    
    @staticmethod
    def axial_round(frac: tuple[float, float]) -> tuple[int, int]:
        q_frac, r_frac = frac
        s_frac = -q_frac - r_frac
        q = round(q_frac)
        r = round(r_frac)
        s = round(s_frac)

        q_diff = abs(q - q_frac)
        r_diff = abs(r - r_frac)
        s_diff = abs(s - s_frac)

        if q_diff > r_diff and q_diff > s_diff:
            q = -r-s
        elif r_diff > s_diff:
            r = -q-s    

        return (q, r)
