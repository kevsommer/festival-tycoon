MAX_ZOOM = 2
MIN_ZOOM = 0.5

WINDOW_OFFSET_X = 960
WINDOW_OFFSET_Y = 540

class ViewportTransformer:
    def __init__(self):
        self.zoom = 1
        self.zoom_factor = 0.1
    
    def zoom_in(self):
        self.zoom = min(self.zoom + self.zoom_factor, MAX_ZOOM)
    
    def zoom_out(self):
        self.zoom = max(self.zoom - self.zoom_factor, MIN_ZOOM)

    def transform_to_screen_coords(self, x, y):
        return x * self.zoom + WINDOW_OFFSET_X, y * self.zoom + WINDOW_OFFSET_Y
    
    def transform_to_world_coords(self, x, y):
        return (x - WINDOW_OFFSET_X) / self.zoom, (y - WINDOW_OFFSET_Y) / self.zoom
