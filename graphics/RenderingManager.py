import pygame
from assets.colors import COLORS
from state.Tile import Tile, TileId
from graphics.Camera import Camera
from state.MapStateManager import MapStateManager

type Tile = tuple[TileId, Tile]

class RenderingManager:
    def draw_hex_map(self, 
                     map_state_manager: MapStateManager,
                     camera: Camera, 
                     screen: pygame.Surface):
        
        for tile in map_state_manager.tiles.items():
            self.draw_tile(tile, map_state_manager, camera, screen)
        
        selected_tile_id = map_state_manager.selected_tile
        if selected_tile_id is not None:
            selected_tile = map_state_manager.tiles[map_state_manager.selected_tile]
            
            self.draw_tile((selected_tile_id, selected_tile), map_state_manager, camera, screen, selected=True)
    
    def get_color(self, tile: Tile):
        if tile.__class__.__name__ == 'StageTile':
            return COLORS['yellow']
        
        if tile.terrain == 'water':
            return COLORS['blue']
        elif tile.terrain == 'grass':
            return COLORS['green']
        elif tile.terrain == 'mountain':
            return COLORS['gray']
        return COLORS['black']
    
    def draw_tile(self, 
                  tile: Tile, 
                  map_state_manager: MapStateManager,
                  camera: Camera, 
                  screen: pygame.Surface, 
                  selected: bool = False):
        
        tile_id, tile = tile
        
        hex_tile = map_state_manager.get_hex_tile(tile_id)
        color = self.get_color(tile)
        hex_tile_points = list(map(camera.transform_to_screen_coords, hex_tile.points))

        pygame.draw.polygon(screen, color, hex_tile_points)
        
        if selected: 
            width = round(camera.zoom * 5)
            pygame.draw.polygon(screen, COLORS['red'], hex_tile_points, width=width)
        