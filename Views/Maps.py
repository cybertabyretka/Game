class TileMap:
    def __init__(self, width, height, tile_size, assets):
        self.width = width
        self.height = height
        self.tile_size = tile_size
        self.tile_map = {}
        self.collision_map = {}
        self.assets = assets

    def render(self, surface):
        for loc in self.tile_map:
            tile = self.tile_map[loc]
            tile.render(surface, tuple(map(float, loc.split(';'))))


class Tile:
    def __init__(self, image, kind: str, variant: int, obstruction: float, size=(35, 35)):
        self.image = image
        self.kind: str = kind
        self.variant: int = variant
        self.size = size
        self.obstruction = obstruction

    def render(self, surface, pos):
        surface.blit(self.image, pos)