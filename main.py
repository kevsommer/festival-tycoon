import pygame
from assets.colors import COLORS
from core.EventHandler import EventHandler
from core.HexTileMap import HexTileMap
from graphics.RenderingManager import RenderingManager
from graphics.ViewportTransformer import ViewportTransformer
from state.MapStateManager import MapStateManager
from core.AxialHexCoord import AxialHexCoord

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
                axial_mouse_pos = AxialHexCoord.pixel_to_hex(
                    self.viewport_transformer.transform_to_world_coords(mouse_pos)
                )

                self.map_state_manager.handle_tile_click(axial_mouse_pos)

    def draw(self):
        self.rendering_manager.draw_hex_map(self.map_state_manager, self.hex_tile_map, self.viewport_transformer, self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()
