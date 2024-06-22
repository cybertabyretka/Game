import pygame as pg


class InGameWindowV:
    def __init__(self, colour, name, start_pos, size):
        self.rect = pg.Rect(start_pos, size)
        self.colour = colour
        self.name = name

    def draw(self, surface, content_view, content=None):
        pg.draw.rect(surface, self.colour, self.rect)
        self.name.view.draw(surface, self.rect)
        if content is not None:
            content_view.draw(surface, content, (self.rect.topleft[0], self.rect.topleft[1] + self.name.view.font_size))