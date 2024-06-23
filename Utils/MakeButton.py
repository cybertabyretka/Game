import pygame as pg

from Models.Text import Text
from Models.InteractionObjects.Button import Button


def make_button(x: int, y: int, width: int, height: int, thickness: int, colour_if_selected: tuple[int, int, int], colour_if_unselected: tuple[int, int, int], text: str, text_colour: tuple[int, int, int], font_size: int, font_path: str) -> Button:
    return Button(pg.Rect(x, y, width, height), thickness, colour_if_selected, colour_if_unselected, Text(text, text_colour, font_size, font_path))
