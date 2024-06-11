class GameV:
    def __init__(self, display, rooms_map):
        self.display = display
        self.rooms_map = rooms_map

    def render(self):
        self.rooms_map.get_current_room().render(self.display.surface)