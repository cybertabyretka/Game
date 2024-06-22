import pygame as pg

from BaseVariables.TileMapOffsets import NEIGHBOUR_OFFSETS
from BaseVariables.Others import TILE_SIZE

from Controllers.Weapons.Projectiles.BaseProjectilePhysic import *
from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around


class FireBallPhysic(BaseProjectilePhysic):
    def __init__(self, size, max_velocity, damage_types):
        super().__init__(size, max_velocity, damage_types, FireBallCollision)

    def copy(self):
        copied_physic = FireBallPhysic((self.collision.rect.w, self.collision.rect.h), self.max_velocity, self.damage_types)
        copied_physic.direction = self.direction
        return copied_physic


class FireBallCollision(BaseProjectileCollision):
    pass