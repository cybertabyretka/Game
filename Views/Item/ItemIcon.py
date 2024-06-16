from Utils.Singleton import Singleton
from Utils.Settings.Icons.Icons import EMPTY_ICON


class Icon:
    def __init__(self, image_path):
        self.image_path = image_path
        self.image = None

    def draw(self, surface, start_pos):
        surface.blit(self.image, start_pos)


class EmptyIcon(Icon, Singleton):
    def __init__(self):
        super().__init__(EMPTY_ICON)