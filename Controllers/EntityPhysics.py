import pygame as pg


class EntityPhysics:
    def __init__(self, width, height, start_pos=(10., 10.), max_velocity=1):
        self.collision = PlayerCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    def update_collision(self):
        self.collision.rect[0] += self.velocity[0]
        self.collision.rect[1] += self.velocity[1]


class PlayerCollision:
    def __init__(self, pos, size):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos=(10., 10.), max_velocity=1):
        super().__init__(width, height, start_pos, max_velocity)
