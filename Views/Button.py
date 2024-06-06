import pygame as pg


class ButtonV:
    def __init__(self, rect, selected_rect_colour, unselected_rect_colour, text):
        self.rect = rect
        self.selected_rect_colour = selected_rect_colour
        self.unselected_rect_colour = unselected_rect_colour
        self.text = text
        self.selected = False

    def render(self, surface):
        if self.selected:
            pg.draw.rect(surface, self.selected_rect_colour, self.rect)
        else:
            pg.draw.rect(surface, self.unselected_rect_colour, self.rect)
        self.text.view.render(surface, self.rect)