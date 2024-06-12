import pygame as pg

from Views.InGameWindow import InGameWindowV


class InGameWindow:
    def __init__(self, name, size, start_pos, colour):
        self.view = InGameWindowV(colour, name, start_pos, size)
