import pygame as pg


class TileCollision:
    def __init__(self, cross_ability: int, pos: tuple[int, int], size: tuple[int, int]):
        self.cross_ability: int = cross_ability
        self.rect: pg.Rect = pg.Rect(pos[0], pos[1], size[0], size[1])
