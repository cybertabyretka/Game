from Views.Image import load_image


class FireBallV:
    def __init__(self, image_path):
        self.path = image_path
        self.image = None

    def download_images(self):
        self.image = load_image(self.path, True, (122, 0, 12))

    def draw(self, start_pos, surface):
        surface.blit(self.image, start_pos)