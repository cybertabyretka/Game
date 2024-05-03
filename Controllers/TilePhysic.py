import pygame as pg


class TileCollision:
    def __init__(self, obstruction, pos, size):
        self.obstruction = obstruction
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])