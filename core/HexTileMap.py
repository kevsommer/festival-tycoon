from .HexTile import HexTile
from .AxialHexCoord import AxialHexCoord

class HexTileMap: 
    def __init__(self):
        self.hex_axials = self.gen_hex_axials(6)
        self.hex_tiles = {}
        
        for axials in self.hex_axials:
            tile_id = (axials.q, axials.r)
            self.hex_tiles[tile_id] = HexTile(axials.x, axials.y)
            
    # generate all hex axials within a certain radius of a hexagon
    def gen_hex_axials(self, N):
        hex_axials = []
        for q in range(-N, N+1):
            for r in range(max(-N, -q-N), min(N, -q+N)+1):
                hex_axials.append((q, r))
        
        return list(map(lambda axial: AxialHexCoord(axial[0], axial[1]), hex_axials))

    def get_hex_tile(self, tile_id):
        if tile_id in self.hex_tiles:
            return self.hex_tiles[tile_id]
        return None
