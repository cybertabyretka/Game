import pygame as pg


class ButtonV:
    def __init__(self, rect, rect_colour, text):
        self.rect = rect
        self.rect_colour = rect_colour
        self.text = text

    def render(self, surface):
        pg.draw.rect(surface, self.rect_colour, self.rect)
        self.text.view.render(surface, self.rect)