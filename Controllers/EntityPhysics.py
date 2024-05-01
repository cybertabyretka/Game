from Models import Entities
from abc import ABC


class PhysicsEntity(ABC):
    def update_pos(self):
        pass

    def attack(self):
        pass


class PlayerPhysicsEntity(PhysicsEntity):
    def __init__(self, entity):
        self.entity: Entities.Entity = entity

    def update_pos(self):
        self.entity.collision[0] += self.entity.velocity[0]
        self.entity.collision[1] += self.entity.velocity[1]

    def attack(self):
        pass