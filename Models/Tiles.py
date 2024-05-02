from Controllers.TilePhysics import TileCollision


class Tile:
    def __init__(self, image, kind: str, variant: int, obstruction: float, pos: tuple[float, float], size=(35, 35)):
        self.image = image
        self.kind: str = kind
        self.variant: int = variant
        self.size = size
        self.collision = TileCollision(obstruction, pos, size)
