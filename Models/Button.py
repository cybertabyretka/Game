import pygame as pg

from Models.Text import Text

from Views.Button import ButtonV


class Button:
    def __init__(self, rect, thickness, rect_colour1, rect_colour2, text):
        self.view = ButtonV(rect, thickness, rect_colour1, rect_colour2, text)


def make_button(x, y, width, height, thickness, colour_if_selected, colour_if_unselected, text, text_colour, font_size, font_path):
    return Button(pg.Rect(x, y, width, height), thickness, colour_if_selected, colour_if_unselected, Text(text, text_colour, font_size, font_path))