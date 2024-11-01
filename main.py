import pygame
from core.HexTileMap import HexTileMap
from state.MapStateManager import MapStateManager
from graphics.RenderingManager import RenderingManager
from graphics.ViewportTransformer import ViewportTransformer
from assets.colors import COLORS

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.running = True
        self.hex_tile_map = HexTileMap()
        self.map_state_manager = MapStateManager(self.hex_tile_map)
        self.rendering_manager = RenderingManager()
        self.viewport_transformer = ViewportTransformer()

    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        self.viewport_transformer.zoom_in()
                    if event.key == pygame.K_DOWN:
                        self.viewport_transformer.zoom_out()
        
            self.screen.fill(COLORS['black'])
            self.update()
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.rendering_manager.draw_hex_map(self.map_state_manager, self.hex_tile_map, self.viewport_transformer, self.screen)

    def update(self):
        self.handle_mouse_click()

    def handle_mouse_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:

            for (tile_id, tile) in self.hex_tile_map.hex_tiles.items():
                mouse_x, mouse_y = self.viewport_transformer.transform_to_world_coords(mouse_pos[0], mouse_pos[1])
                if tile.check_if_inside_hexagon(mouse_x, mouse_y):
                    self.map_state_manager.handle_tile_click(tile_id)

if __name__ == "__main__":
    game = Game()
    game.run()
