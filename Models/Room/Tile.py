from Views.Room.Tile import TileV
from Controllers.TilePhysic import TileCollision


class Tile:
    def __init__(self, path, cross_ability: int, pos: tuple[int, int], size=(35, 35)):
        self.view = TileV(path)
        self.collision = TileCollision(cross_ability, pos, size)

    def copy_for_save(self):
        return Tile(self.view.path, self.collision.cross_ability, self.collision.rect.topleft, (self.collision.rect.width, self.collision.rect.height))


class LootTile(Tile):
    def __init__(self, pos: tuple[int, int], inventory, size=(35, 35)):
        super().__init__(None, 1, pos, size)
        self.inventory = inventory

    def download_images(self):
        self.inventory.download_images()

    def copy_for_save(self):
        return LootTile(self.collision.rect.topleft, self.inventory.copy_for_save(), (self.collision.rect.width, self.collision.rect.height))