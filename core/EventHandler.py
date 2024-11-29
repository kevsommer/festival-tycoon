import pygame

class EventHandler:
    def __init__(self):
        self.dragging = False
        self.drag_start_pos = (0, 0)
        self.actions = []
    
    def handle_event(self, event):
        self.actions = []

        self.handle_zoom(event)
        self.handle_mouse(event)
        self.handle_mouse_click()
        
        return self.actions

    def handle_zoom(self, event):
        if event.type == pygame.MOUSEWHEEL:
            if event.y < 0:
                self.actions.append(('zoom_out', None))
            else:
                self.actions.append(('zoom_in', None))

    def handle_mouse(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 and not self.dragging:
            self.dragging = True
            self.drag_start_pos = pygame.mouse.get_pos()

        if event.type == pygame.MOUSEBUTTONUP and self.dragging and event.button == 1:
            self.dragging = False
        
        if event.type == pygame.MOUSEMOTION and self.dragging:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            dx = mouse_x - self.drag_start_pos[0]
            dy = mouse_y - self.drag_start_pos[1]
            self.drag_start_pos = (mouse_x, mouse_y)

            self.actions.append(('move', (dx, dy)))

    def handle_mouse_click(self):
        mouse_pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0]:
            self.actions.append(('click', mouse_pos))
