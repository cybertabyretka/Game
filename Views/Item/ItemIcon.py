from Utils.Singleton import Singleton
from Utils.Image import load_image

from Models.Assets.PathsAsset import EMPTY_ITEM


class Icon:
    def __init__(self, paths_asset):
        self.paths_assets = paths_asset
        self.image = None

    def download_images(self):
        self.image = load_image(self.paths_assets['icon'], set_colour=True, colour_to_change=(120, 0, 12))

    def copy_for_save(self):
        return Icon(self.paths_assets)

    def draw(self, surface, start_pos):
        surface.blit(self.image, start_pos)


class EmptyIcon(Icon, Singleton):
    def __init__(self):
        super().__init__(EMPTY_ITEM)

    def copy_for_save(self):
        return EmptyIcon()
