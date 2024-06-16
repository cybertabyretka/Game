import pygame as pg

from Utils.Setting import get_font


class TextV:
    def __init__(self, text, text_colour, font_size, font_path):
        self.text = text
        self.colour = text_colour
        self.font_size = font_size
        self.font_path = font_path

    def change_font(self, font_size=None, font_path=None):
        if font_size is not None:
            self.font_size = font_size
        if font_path is not None:
            self.font_path = font_path

    def render(self, surface: pg.Surface, rect):
        rendered_text = get_font(self.font_path, self.font_size).render(self.text, True, self.colour)
        surface.blit(rendered_text, rect)