from Views.Room.Tile import TileV
from Controllers.TilePhysic import TileCollision


class Tile:
    def __init__(self, image, cross_ability: int, pos: tuple[int, int], size=(35, 35)):
        self.view = TileV(image)
        self.collision = TileCollision(cross_ability, pos, size)


class LootTile(Tile):
    def __init__(self, image, cross_ability: int, pos: tuple[int, int], inventory, size=(35, 35)):
        super().__init__(image, cross_ability, pos, size)
        self.inventory = inventory