import pygame as pg

from Models.Text import Text


class InGameWindowV:
    def __init__(self, colour: tuple[int, int, int], name: Text, start_pos: tuple[int, int], size: tuple[int, int]):
        self.rect: pg.Rect = pg.Rect(start_pos, size)
        self.colour: tuple[int, int, int] = colour
        self.name: Text = name

    def draw(self, surface: pg.Surface, content_view, content=None) -> None:
        pg.draw.rect(surface, self.colour, self.rect)
        self.name.view.draw(surface, self.rect)
        if content is not None:
            content_view.draw(surface, content, (self.rect.topleft[0], self.rect.topleft[1] + self.name.view.font_size))
