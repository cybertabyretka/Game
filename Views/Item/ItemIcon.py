from Utils.Setting import EMPTY_ICON


class Icon:
    def __init__(self, image, size):
        self.image = image
        self.size = size

    def draw(self, surface, start_pos):
        surface.blit(self.image, start_pos)


class EmptyIcon(Icon):
    def __init__(self, size):
        super().__init__(EMPTY_ICON, size)