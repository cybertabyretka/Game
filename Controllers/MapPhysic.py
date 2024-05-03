class CollisionsMap:
    def __init__(self):
        self.map = {}

    def get_map_from_object(self, tile_map):
        for loc in tile_map:
            tile = tile_map[loc]
            self.map[loc] = tile.collision
