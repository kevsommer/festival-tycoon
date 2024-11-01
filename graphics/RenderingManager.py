import pygame
from assets.colors import COLORS
class RenderingManager:
    def draw_hex_map(self, map_state_manager, hex_tile_map, viewport_transformer, screen):
        for (tile_id, tile_state) in map_state_manager.tile_states.items():
            hex_tile = hex_tile_map.get_hex_tile(tile_id)
            self.draw_hex_tile(hex_tile, screen, terrain=tile_state.terrain, viewport_transformer=viewport_transformer)
            
        if map_state_manager.selected_tile is not None:
            selected_hex_tile = hex_tile_map.get_hex_tile(map_state_manager.selected_tile)
            self.draw_selected_tile(selected_hex_tile, screen, viewport_transformer)

    def get_terrain_color(self, terrain):
        if terrain == 'water':
            return COLORS['blue']
        elif terrain == 'grass':
            return COLORS['green']
        elif terrain == 'mountain':
            return COLORS['gray']
        return COLORS['black']
    
    def draw_hex_tile(self, hex_tile, screen, terrain, viewport_transformer):
        color = self.get_terrain_color(terrain)

        hex_tile_points = [viewport_transformer.transform_to_screen_coords(x, y) for (x, y) in hex_tile.points]
        pygame.draw.polygon(screen, color, hex_tile_points)

    def draw_selected_tile(self, hex_tile, screen, viewport_transformer):
        hex_tile_points = [viewport_transformer.transform_to_screen_coords(x, y) for (x, y) in hex_tile.points]
        pygame.draw.polygon(screen, COLORS['red'], hex_tile_points, width=5)
