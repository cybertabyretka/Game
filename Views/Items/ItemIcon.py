from Utils.Singleton import Singleton
from Utils.Image import load_image

from BaseVariables.Assets.PathsAsset import EMPTY_ICON


class Icon:
    def __init__(self, path: str):
        self.path = path
        self.image = None

    def download_images(self):
        self.image = load_image(self.path, set_colour=True, colour_to_change=(120, 0, 12))

    def copy_for_save(self):
        return Icon(self.path)

    def draw(self, surface, start_pos):
        surface.blit(self.image, start_pos)


class EmptyIcon(Icon, Singleton):
    def __init__(self):
        super().__init__(EMPTY_ICON['icon'])

    def copy_for_save(self):
        return EmptyIcon()
