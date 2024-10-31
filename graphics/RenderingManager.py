import pygame

class RenderingManager:
    def draw_hex_map(self, map_state_manager, hex_tile_map, screen):
        for tile_state in map_state_manager.tile_states:
            hex_tile = hex_tile_map.get_hex_tile(tile_state.id)
            self.draw_hex_tile(hex_tile, screen, terrain=tile_state.terrain)

    def get_terrain_color(self, terrain):
        if terrain == 'water':
            return (0, 0, 255)
        elif terrain == 'grass':
            return (0, 255, 0)
        elif terrain == 'mountain':
            return (128, 128, 128)
        return (0, 0, 0)
    
    def draw_hex_tile(self, hex_tile, screen, terrain):
        color = self.get_terrain_color(terrain)

        pygame.draw.polygon(screen, color, hex_tile.points)
