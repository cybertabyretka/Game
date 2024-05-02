from Models import Entities
from abc import ABC
import pygame as pg


class EntityPhysics(ABC):
    def update_pos(self):
        pass

    def attack(self):
        pass


class PlayerCollision:
    def __init__(self, pos, size):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])

    def update_collision(self, velocity):
        self.rect[0] += velocity[0]
        self.rect[1] += velocity[1]


class PlayerPhysics(EntityPhysics):
    def __init__(self, entity, start_pos=(10., 10.), max_velocity=1):
        self.entity: Entities.Entity = entity
        self.collision = PlayerCollision(start_pos, (entity.width, entity.height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    def attack(self):
        pass