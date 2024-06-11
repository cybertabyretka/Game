class GameV:
    def __init__(self, surface, rooms_map):
        self.surface = surface
        self.rooms_map = rooms_map

    def render(self):
        self.rooms_map.get_current_room().render(surface)