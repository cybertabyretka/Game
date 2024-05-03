class RoomV:
    def __init__(self, tile_map, pos, tile_size):
        self.tile_map = tile_map
        self.tile_size = tile_size
        self.pos = pos

    def render_tile_map(self, surface):
        for loc in self.tile_map.tile_map:
            tile = self.tile_map.tile_map[loc]
            tile.tile_view.render(surface, tuple(map(float, loc.split(';')))[::-1])