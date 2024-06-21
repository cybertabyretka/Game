class GameV:
    def __init__(self, display, rooms_map):
        self.display = display
        self.rooms_map = rooms_map

    def render(self, room, buttons=None):
        room.view.render_tile_map(self.display.surface)
        if buttons is not None:
            for button in buttons:
                button.view.render(self.display.surface)