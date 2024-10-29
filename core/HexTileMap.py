from .HexTileSprite import HexTileSprite
from .AxialHexCoord import AxialHexCoord

class HexTileMap: 
    def __init__(self):
        self.hex_axials = self.gen_hex_axials(6)
        self.hex_tile_sprites = []

        for axials in self.hex_axials:
            self.hex_tile_sprites.append(HexTileSprite(axials.x, axials.y))
            
    # generate all hex axials within a certain radius of a hexagon
    def gen_hex_axials(self, N):
        hex_axials = []
        for q in range(-N, N+1):
            for r in range(max(-N, -q-N), min(N, -q+N)+1):
                hex_axials.append((q, r))
        
        return list(map(lambda axial: AxialHexCoord(axial[0], axial[1]), hex_axials))

    def draw(self, screen):
        for hex_tile_sprite in self.hex_tile_sprites:
            hex_tile_sprite.draw(screen)

