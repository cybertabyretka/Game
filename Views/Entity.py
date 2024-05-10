from Utils.Picture import Picture
from Utils.Picture import load_image


class EntityV:
    def __init__(self, image_path: str):
        self.image: Picture = load_image(image_path)

    def render(self, surface, pos):
        surface.blit(self.image.surface, pos)

    @staticmethod
    def clear_surface(surface, base_colour=(0, 0, 0)):
        surface.fill(base_colour)
