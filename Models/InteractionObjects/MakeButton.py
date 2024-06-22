import pygame as pg

from Models.Text import Text
from Models.InteractionObjects.Button import Button


def make_button(x, y, width, height, thickness, colour_if_selected, colour_if_unselected, text, text_colour, font_size, font_path):
    return Button(pg.Rect(x, y, width, height), thickness, colour_if_selected, colour_if_unselected, Text(text, text_colour, font_size, font_path))