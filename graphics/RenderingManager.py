import pygame
from assets.colors import COLORS
from core.HexTile import HexTile
from core.HexTileMap import HexTileMap
from state.TileState import TileState, TileId
from graphics.ViewportTransformer import ViewportTransformer
from state.MapStateManager import MapStateManager

type Tile = tuple[TileId, TileState]

class RenderingManager:
    def draw_hex_map(self, 
                     map_state_manager: MapStateManager,
                     hex_tile_map: HexTileMap,
                     viewport_transformer: ViewportTransformer, 
                     screen: pygame.Surface):
        
        for tile in map_state_manager.tile_states.items():
            selected = True if map_state_manager.selected_tile == tile[0] else False
            self.draw_tile(tile, hex_tile_map, viewport_transformer, screen, selected)
        
        selected_tile_id = map_state_manager.selected_tile
        if selected_tile_id is not None:
            selected_tile = map_state_manager.tile_states[map_state_manager.selected_tile]
            
            self.draw_tile((selected_tile_id, selected_tile), hex_tile_map, viewport_transformer, screen, selected=True)
    
    def get_color(self, tile_state: TileState):
        if tile_state.__class__.__name__ == 'StageTile':
            return COLORS['yellow']
        
        if tile_state.terrain == 'water':
            return COLORS['blue']
        elif tile_state.terrain == 'grass':
            return COLORS['green']
        elif tile_state.terrain == 'mountain':
            return COLORS['gray']
        return COLORS['black']
    
    def draw_tile(self, 
                  tile: Tile, 
                  hex_tile_map: HexTileMap, 
                  viewport_transformer: ViewportTransformer, 
                  screen: pygame.Surface, selected: bool):
        
        tile_id, tile_state = tile
        
        hex_tile = hex_tile_map.get_hex_tile(tile_id)
        color = self.get_color(tile_state)
        hex_tile_points = list(map(viewport_transformer.transform_to_screen_coords, hex_tile.points))

        pygame.draw.polygon(screen, color, hex_tile_points)
        
        if selected: 
            width = round(viewport_transformer.zoom * 5)
            pygame.draw.polygon(screen, COLORS['red'], hex_tile_points, width=width)
        