import pygame as pg

from Utils.Setting import get_font


class TextV:
    def __init__(self, text, text_colour, font_size, font_path):
        self.text = text
        self.colour = text_colour
        self.font_size = font_size
        self.font_path = font_path
        self.font = get_font(font_path, font_size)

    def change_font(self, font_size=None, font_path=None):
        font_is_changed = False
        if font_size is not None:
            self.font_size = font_size
            font_is_changed = True
        if font_path is not None:
            self.font_path = font_path
            font_is_changed = True
        if font_is_changed:
            self.font = get_font(self.font_path, self.font_size)

    def render(self, surface: pg.Surface, rect):
        rendered_text = self.font.render(self.text, True, self.colour)
        surface.blit(rendered_text, rect)