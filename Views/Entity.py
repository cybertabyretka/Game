class EntityV:
    def __init__(self, image):
        self.image = image

    def render(self, surface, pos):
        surface.blit(self.image, pos)

    @staticmethod
    def clear_surface(surface, base_colour=(0, 0, 0)):
        surface.fill(base_colour)
