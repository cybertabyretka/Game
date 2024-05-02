import pygame as pg


class RoomV:
    def __init__(self, size, pos):
        self.surface = pg.Surface(size)
        self.pos = pos

    def render(self, surface):
        surface.blit(self.surface, self.pos)