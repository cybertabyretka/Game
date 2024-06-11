from Utils.TileMap import create_base_tile_map


class RoomsMap:
    def __init__(self, size):
        self.map = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.current_index = (0, 0)

    def make_room(self, indexes, width=None, height=None, tiles_size=None, assets=None, tile_map=None):
        if tile_map is None:
            tile_map = create_base_tile_map(width, height, tiles_size, assets)
        self.map[indexes[0]][indexes[1]] = tile_map

    def get_current_room(self):
        return self.map[self.current_index[0]][self.current_index[1]]

    def render_current_room(self, surface):
        self.get_current_room().render_tile_map(surface)
