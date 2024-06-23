import pygame as pg

from Models.Text import Text


class ButtonV:
    def __init__(self, rect: pg.Rect, thickness: int, selected_rect_colour: tuple[int, int, int], unselected_rect_colour: tuple[int, int, int], text: Text):
        self.rect: pg.Rect = rect
        self.thickness: int = thickness
        self.selected_rect_colour: tuple[int, int, int] = selected_rect_colour
        self.unselected_rect_colour: tuple[int, int, int] = unselected_rect_colour
        self.text: Text = text
        self.selected: bool = False

    def draw(self, surface: pg.Surface) -> None:
        if self.selected:
            pg.draw.rect(surface, self.selected_rect_colour, self.rect, self.thickness)
        else:
            pg.draw.rect(surface, self.unselected_rect_colour, self.rect, self.thickness)
        self.text.view.draw(surface, self.rect)
