import pygame

class RenderingManager:
    def draw_hex_map(self, map_state_manager, hex_tile_map, screen):
        for tile_state in map_state_manager.tile_states:
            hex_tile = hex_tile_map.get_hex_tile(tile_state.id)
            self.draw_hex_tile(hex_tile, screen, terrain=tile_state.terrain)
            
        if map_state_manager.selected_tile is not None:
            selected_hex_tile = hex_tile_map.get_hex_tile(map_state_manager.selected_tile)
            self.draw_selected_tile(selected_hex_tile, screen)

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

    def draw_selected_tile(self, hex_tile, screen):
        pygame.draw.polygon(screen, (255, 0, 0), hex_tile.points, width=5)
