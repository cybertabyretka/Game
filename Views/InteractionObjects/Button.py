import pygame as pg


class ButtonV:
    def __init__(self, rect, thickness, selected_rect_colour, unselected_rect_colour, text):
        self.rect = rect
        self.thickness = thickness
        self.selected_rect_colour = selected_rect_colour
        self.unselected_rect_colour = unselected_rect_colour
        self.text = text
        self.selected = False

    def draw(self, surface):
        if self.selected:
            pg.draw.rect(surface, self.selected_rect_colour, self.rect, self.thickness)
        else:
            pg.draw.rect(surface, self.unselected_rect_colour, self.rect, self.thickness)
        self.text.view.draw(surface, self.rect)