import pygame
from assets.colors import COLORS
from core.EventHandler import EventHandler
from graphics.RenderingManager import RenderingManager
from graphics.Camera import Camera
from state.MapStateManager import MapStateManager
from core.AxialHexCoord import AxialHexCoord
from assets.constants import SCREEN_WIDTH, SCREEN_HEIGHT

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.running = True
        self.map_state_manager = MapStateManager()
        self.rendering_manager = RenderingManager()
        self.camera = Camera()
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
                self.camera.zoom_out()
            elif action[0] == 'zoom_in':
                self.camera.zoom_in()
            elif action[0] == 'move':
                self.camera.move(action[1][0], action[1][1])
            elif action[0] == 'click':
                mouse_pos: tuple[float, float] = action[1]
                axial_mouse_pos = AxialHexCoord.pixel_to_hex(
                    self.camera.transform_to_world_coords(mouse_pos)
                )

                self.map_state_manager.handle_tile_click(axial_mouse_pos)

    def draw(self):
        self.rendering_manager.draw_hex_map(self.map_state_manager, self.camera, self.screen)
        self.rendering_manager.draw_hud(self.screen, self.map_state_manager)

if __name__ == "__main__":
    game = Game()
    game.run()
