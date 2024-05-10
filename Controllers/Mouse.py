import pygame as pg


class Mouse:
    def __init__(self, num_buttons=3):
        self.mouse = pg.mouse
        self.num_buttons = num_buttons
