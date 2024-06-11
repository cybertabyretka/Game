class TileV:
    def __init__(self, image):
        self.image = image

    def render(self, surface, pos):
        surface.blit(self.image, pos)
