import pygame as pg


class Entity:
    def __init__(self, width: float, height: float):
        self.width: float = width
        self.height: float = height


class Player(Entity):
    def __init__(self, width=20, height=20):
        super().__init__(width, height)
