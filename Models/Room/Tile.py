from Controllers.RoomMap.TilePhysic import TileCollision

from Models.Inventory.Inventory import Inventory

from Views.Room.Tile import TileV


class Tile:
    def __init__(self, path: str | None, cross_ability: int, pos: tuple[int, int], size: tuple[int, int] = (35, 35)):
        self.view: TileV = TileV(path)
        self.collision: TileCollision = TileCollision(cross_ability, pos, size)

    def copy_for_save(self):
        return Tile(self.view.path, self.collision.cross_ability, self.collision.rect.topleft, (self.collision.rect.width, self.collision.rect.height))


class LootTile(Tile):
    def __init__(self, pos: tuple[int, int], inventory: Inventory, size: tuple[int, int] = (35, 35)):
        super().__init__(None, 1, pos, size)
        self.inventory: Inventory = inventory

    def download_images(self) -> None:
        self.inventory.download_images()

    def copy_for_save(self):
        return LootTile(self.collision.rect.topleft, self.inventory.copy_for_save(), (self.collision.rect.width, self.collision.rect.height))
