import pygame as pg


class Display:
    def __init__(self, width: int, height: int, name: str):
        self.display: pg.display = pg.display
        self.surface: pg.Surface = self.display.set_mode((width, height))
        self.display.set_caption(name)
        self.name: str = name

    def update(self) -> None:
        self.display.update()
