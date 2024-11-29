MAX_ZOOM = 2
MIN_ZOOM = 0.5

WINDOW_OFFSET_X = 960
WINDOW_OFFSET_Y = 540

class ViewportTransformer:
    def __init__(self):
        self.zoom = 1
        self.zoom_factor = 0.1
        self.translate_x = 0
        self.translate_y = 0
    
    def zoom_in(self):
        self.zoom = min(self.zoom + self.zoom_factor, MAX_ZOOM)
    
    def zoom_out(self):
        self.zoom = max(self.zoom - self.zoom_factor, MIN_ZOOM)
    
    def move(self, dx, dy):
        self.translate_x += dx
        self.translate_y += dy

    def transform_to_screen_coords(self, x, y):
        return (x * self.zoom + WINDOW_OFFSET_X + self.translate_x), (y * self.zoom + WINDOW_OFFSET_Y + self.translate_y)
    
    def transform_to_world_coords(self, x, y):
        return (x - self.translate_x - WINDOW_OFFSET_X) / self.zoom, (y - self.translate_y - WINDOW_OFFSET_Y) / self.zoom
