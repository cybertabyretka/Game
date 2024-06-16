from Views.Room.Tile import TileV
from Controllers.TilePhysic import TileCollision


class Tile:
    def __init__(self, path, cross_ability: int, pos: tuple[int, int], size=(35, 35)):
        self.type = type
        self.variant = variant
        self.view = TileV(path)
        self.collision = TileCollision(cross_ability, pos, size)


class LootTile(Tile):
    def __init__(self, path, cross_ability: int, pos: tuple[int, int], inventory, size=(35, 35)):
        super().__init__(path, cross_ability, pos, size)
        self.inventory = inventory