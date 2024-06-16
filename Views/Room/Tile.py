from Utils.Image import load_image


class TileV:
    def __init__(self, path):
        self.path = path
        self.image = None

    def download_images(self):
        self.image = load_image(self.path)

    def render(self, surface, pos):
        surface.blit(self.image, pos)
