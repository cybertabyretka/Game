class TileMap:
    def __init__(self):
        self.tile_map = {}

    def copy_for_save(self):
        copied_tile_map = {}
        for coord in self.tile_map:
            copied_tile_map[coord] = self.tile_map[coord].copy_for_save()
        return copied_tile_map
