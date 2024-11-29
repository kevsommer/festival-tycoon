import pygame
from assets.colors import COLORS
from core.EventHandler import EventHandler
from core.HexTileMap import HexTileMap
from graphics.RenderingManager import RenderingManager
from graphics.ViewportTransformer import ViewportTransformer
from state.MapStateManager import MapStateManager

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.running = True
        self.hex_tile_map = HexTileMap()
        self.map_state_manager = MapStateManager(self.hex_tile_map)
        self.rendering_manager = RenderingManager()
        self.viewport_transformer = ViewportTransformer()
        self.event_handler = EventHandler()

    def run(self):
        while self.running:
            actions = []
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()

                actions = self.event_handler.handle_event(event)


            self.screen.fill(COLORS['black'])
            self.update(actions)
            self.draw()
            pygame.display.flip()

    def update(self, actions: tuple[str, tuple[int, int] | None]):
        for action in actions:
            if action[0] == 'zoom_out':
                self.viewport_transformer.zoom_out()
            elif action[0] == 'zoom_in':
                self.viewport_transformer.zoom_in()
            elif action[0] == 'move':
                self.viewport_transformer.move(action[1][0], action[1][1])
            elif action[0] == 'click':
                mouse_pos: tuple[int, int] = action[1]
                for (tile_id, tile) in self.hex_tile_map.hex_tiles.items():
                    mouse_x, mouse_y = self.viewport_transformer.transform_to_world_coords(mouse_pos[0], mouse_pos[1])
                    if tile.check_if_inside_hexagon(mouse_x, mouse_y):
                        self.map_state_manager.handle_tile_click(tile_id)

    def draw(self):
        self.rendering_manager.draw_hex_map(self.map_state_manager, self.hex_tile_map, self.viewport_transformer, self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()
