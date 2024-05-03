import pygame as pg


class TileCollision:
    def __init__(self, cross_ability, pos, size):
        self.cross_ability = cross_ability
        self.size = size
        self.pos = pos
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])