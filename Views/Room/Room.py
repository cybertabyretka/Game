class RoomV:
    def __init__(self, tile_map, tile_size, surface):
        self.tile_map = tile_map
        self.tile_size = tile_size
        self.surface = surface

    def render_tile_map(self, surface):
        for loc in self.tile_map.tile_map:
            self.tile_map.tile_map[loc].tile_view.render(surface, tuple(map(float, loc.split(';'))))