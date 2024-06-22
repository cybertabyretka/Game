import pygame as pg

from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around

from BaseVariables.Others import TILE_SIZE


class BaseProjectilePhysic:
    def __init__(self, size, max_velocity, damage_types, collision_type):
        self.collision = collision_type(pg.Rect((0, 0), size))
        self.max_velocity = max_velocity
        self.velocity = (0, 0)
        self.direction = None
        self.damage_types = damage_types

    def copy(self):
        pass

    def set_attack_rect(self, start_pos, direction):
        self.collision.rect.topleft = start_pos
        self.direction = direction
        if direction == 0:
            self.velocity = (0, -self.max_velocity)
        elif direction == 90:
            self.velocity = (self.max_velocity, 0)
        elif direction == 180:
            self.velocity = (0, self.max_velocity)
        elif direction == 270:
            self.velocity = (-self.max_velocity, 0)


class BaseProjectileCollision:
    def __init__(self, rect):
        self.rect = rect
        self.collisions_around = {}

    def update(self, velocity, room, index, movement=(0, 0)):
        get_collisions_around(self.rect, TILE_SIZE, room.collisions_map.map, self.collisions_around)
        for direction in self.collisions_around:
            if self.collisions_around[direction].rect.colliderect(self.rect) and not self.collisions_around[direction].cross_ability:
                del room.collisions_map.movable_damage_map[index]
                return
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        self.rect.x += movement[0]
        self.rect.y += movement[1]