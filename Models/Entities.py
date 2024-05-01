import pygame as pg


class Entity:
    def __init__(self, collision_width: float, collision_height: float, max_velocity: float, start_pos: tuple[float, float] = (10., 10.)):
        self.collision_width: float = collision_width
        self.collision_height: float = collision_height
        self.collision: pg.Rect = pg.Rect(start_pos[0], start_pos[1], collision_width, collision_height)
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]


class Player(Entity):
    def __init__(self, collision_width=20, collision_height=20, max_velocity=1, start_pos=(10, 10)):
        super().__init__(collision_width, collision_height, max_velocity, start_pos)
