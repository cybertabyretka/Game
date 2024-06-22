import pygame as pg

from Views.InteractionObjects.Button import ButtonV


class Button:
    def __init__(self, rect, thickness, rect_colour1, rect_colour2, text):
        self.view = ButtonV(rect, thickness, rect_colour1, rect_colour2, text)
