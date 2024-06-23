import pygame as pg

from Views.InteractionObjects.Button import ButtonV

from Models.Text import Text


class Button:
    def __init__(self, rect: pg.Rect, thickness: int, rect_colour1: tuple[int, int, int], rect_colour2: tuple[int, int, int], text: Text):
        self.view: ButtonV = ButtonV(rect, thickness, rect_colour1, rect_colour2, text)
