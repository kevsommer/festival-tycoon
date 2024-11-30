from .TileState import TileState, TileId
from .StageTile import StageTile
from core.AxialHexCoord import AxialHexCoord

class MapStateManager:
    def __init__(self):
        hex_axials = self.gen_hex_axials(6)
        
        self.tile_states: dict[TileId, TileState] = {}
        self.selected_tile = None
        
        for coord in hex_axials:
            tile_id = (coord.q, coord.r)
            self.tile_states[tile_id] = TileState(tile_id, coord)

        self.tile_states[(0, 0)] = StageTile((0, 0), AxialHexCoord(0, 0))
        
    # generate all hex axials within a certain radius of a hexagon
    def gen_hex_axials(self, N):
        hex_axials = []
        for q in range(-N, N+1):
            for r in range(max(-N, -q-N), min(N, -q+N)+1):
                hex_axials.append((q, r))
        
        return list(map(lambda axial: AxialHexCoord(axial[0], axial[1]), hex_axials))
                    
    def handle_tile_click(self, tile_id: TileId):
        self.selected_tile = tile_id

    def get_hex_tile(self, tile_id):
        if tile_id in self.tile_states.keys():
            return self.tile_states[tile_id].hex_tile
        return None
