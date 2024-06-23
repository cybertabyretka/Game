from Models.Room.Tile import Tile


class TileMap:
    def __init__(self):
        self.map: dict[str, Tile] = {}

    def copy_for_save(self):
        copied_tile_map = TileMap()
        for coord in self.map:
            copied_tile_map.map[coord] = self.map[coord].copy_for_save()
        return copied_tile_map

    def download_images(self) -> None:
        for coord in self.map:
            self.map[coord].view.download_images()
