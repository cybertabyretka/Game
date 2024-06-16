class TileMap:
    def __init__(self):
        self.map = {}

    def copy_for_save(self):
        copied_tile_map = {}
        for coord in self.map:
            copied_tile_map[coord] = self.map[coord].copy_for_save()
        return copied_tile_map

    def download_images(self):
        for coord in self.map:
            self.map[coord].view.download_images()
