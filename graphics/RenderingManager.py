import pygame
from assets.colors import COLORS
from state.Tile import Tile
from graphics.Camera import Camera
from state.MapStateManager import MapStateManager

class RenderingManager:
    def draw_hex_map(self, map_state_manager: MapStateManager, camera: Camera, screen: pygame.Surface):        

        for tile in map_state_manager.tiles.values():
            tile.draw(screen, camera)
        
        selected_tile_id = map_state_manager.selected_tile
        
        if selected_tile_id is not None:
            selected_tile = map_state_manager.tiles[map_state_manager.selected_tile]
            selected_tile.draw(screen, camera, selected=True)
    
    def get_color(self, tile: Tile) -> tuple[int, int, int]:
        if tile.__class__.__name__ == 'StageTile':
            return COLORS['yellow']
        
        if tile.terrain == 'water':
            return COLORS['blue']
        elif tile.terrain == 'grass':
            return COLORS['green']
        elif tile.terrain == 'mountain':
            return COLORS['gray']
        return COLORS['black']
    