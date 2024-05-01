from Models import Entities
from abc import ABC


class PhysicsEntity(ABC):
    def __init__(self):
        pass



class PlayerPhysicsEntity(PhysicsEntity):
    def __init__(self, entity):
        self.entity: Entities.Entity = entity
        self.velocity: list[float] = [0., 0.]

    def update_pos(self, movement: tuple[float, float] = (0., 0.)):
        frame_movement = (movement[0] + self.velocity[0], movement[1] + self.velocity[1])
        self.entity.collision[0] += frame_movement[0]
        self.entity.collision[1] += frame_movement[1]