from .TileState import TileState

class MapStateManager:
    def __init__(self, hex_tile_map):
        self.tile_states = []

        for axial_coord in hex_tile_map.hex_axials:
            tile_id = (axial_coord.q, axial_coord.r)
            self.tile_states.append(TileState(tile_id))
