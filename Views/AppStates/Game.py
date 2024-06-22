class GameV:
    def __init__(self, display, rooms_map):
        self.display = display
        self.rooms_map = rooms_map

    def draw(self, room, buttons=None):
        room.view.render_tile_map(self.display.surface)
        if buttons is not None:
            for button in buttons:
                button.view.draw(self.display.surface)