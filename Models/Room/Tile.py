from Views.Room.Tile import TileV
from Controllers.TilePhysic import TileCollision


class Tile:
    def __init__(self, image, kind: str, variant: int, cross_ability: float, pos: tuple[float, float], size=(35, 35)):
        self.tile_view = TileV(image)
        self.kind: str = kind
        self.variant: int = variant
        self.collision = TileCollision(cross_ability, pos, size)
