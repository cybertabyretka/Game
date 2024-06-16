class TileV:
    def __init__(self, path):
        self.path = path
        self.image = None

    def render(self, surface, pos):
        surface.blit(self.image, pos)
