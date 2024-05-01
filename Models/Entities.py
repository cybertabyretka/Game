import pygame as pg


class Entity:
    def __init__(self, collision_width: float, collision_height: float, start_pos: tuple[float, float] = (10., 10.)):
        self.collision_width: float = collision_width
        self.collision_height: float = collision_height
        self.collision: pg.Rect = pg.Rect(start_pos[0], start_pos[1], collision_width, collision_height)
        self.x_movement = [False, False]
        self.y_movement = [False, False]


class Player(Entity):
    def __init__(self, collision_width, collision_height, start_pos=(10, 10)):
        super().__init__(collision_width, collision_height, start_pos)
