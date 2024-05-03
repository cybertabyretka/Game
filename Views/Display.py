import pygame as pg


class Display:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.display = pg.display
        self.surface = self.display.set_mode((width, height))
        self.display.set_caption(name)
        self.name = name

    def update(self):
        self.display.update()
