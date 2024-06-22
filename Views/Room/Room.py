class RoomV:
    def __init__(self, tile_map, tile_size):
        self.tile_map = tile_map
        self.tile_size = tile_size

    def render_tile_map(self, surface):
        for loc in self.tile_map.map:
            self.tile_map.map[loc].view.draw(surface, tuple(map(float, loc.split(';'))))