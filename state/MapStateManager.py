from .TileState import TileState

class MapStateManager:
    def __init__(self, hex_tile_map):
        self.tile_states = {}
        self.selected_tile = None

        for axial_coord in hex_tile_map.hex_axials:
            tile_id = (axial_coord.q, axial_coord.r)
            self.tile_states[tile_id] = TileState(tile_id)

    def handle_tile_click(self, tile_id):
        self.selected_tile = tile_id
