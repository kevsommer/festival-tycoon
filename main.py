import pygame
from core.HexTileMap import HexTileMap

class Game: 
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((1920, 1080))
        self.running = True
        self.hex_tile_map = HexTileMap()


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
        
            self.screen.fill((0, 0, 0))
            self.draw()
            pygame.display.flip()

    def draw(self):
        self.hex_tile_map.draw(self.screen)

if __name__ == "__main__":
    game = Game()
    game.run()
