from .TileState import TileState, TileId
from .StageTile import StageTile
from core.AxialHexCoord import AxialHexCoord

# generate all hex axials within a certain radius of a hexagon
def gen_hex_axials(N: int) -> list[AxialHexCoord]:
    hex_axials = []
    for q in range(-N, N+1):
        for r in range(max(-N, -q-N), min(N, -q+N)+1):
            hex_axials.append((q, r))
    
    return list(map(lambda axial: AxialHexCoord(axial[0], axial[1]), hex_axials))

def initialise_tile_states() -> dict[TileId, TileState]:
    hex_axials = gen_hex_axials(6)
    
    tile_states: dict[TileId, TileState] = {}
    
    for coord in hex_axials:
        tile_id = (coord.q, coord.r)
        if tile_id == (0, 0):
            tile_states[tile_id] = StageTile(tile_id, coord)
        else:
            tile_states[tile_id] = TileState(tile_id, coord)
    
    return tile_states

class MapStateManager:
    def __init__(self):
        self.tile_states = initialise_tile_states()
        self.selected_tile = None
        
    def handle_tile_click(self, tile_id: TileId):
        self.selected_tile = tile_id

    def get_hex_tile(self, tile_id):
        if tile_id in self.tile_states.keys():
            return self.tile_states[tile_id].hex_tile
        return None
