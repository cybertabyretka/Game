from Constants.Colours import RGB_FOR_BACKGROUND

from Utils.Image import load_image


class BaseProjectileV:
    def __init__(self, image_path):
        self.path = image_path
        self.image = None

    def download_images(self):
        self.image = load_image(self.path, True, RGB_FOR_BACKGROUND)

    def draw(self, start_pos, surface):
        surface.blit(self.image, start_pos)