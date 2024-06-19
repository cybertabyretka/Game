import pygame as pg

from Utils.Setting import NEIGHBOUR_OFFSETS


class FireBallPhysic:
    def __init__(self, size, max_velocity, damage_types):
        self.collision = FireBallCollision(pg.Rect((0, 0), size))
        self.max_velocity = max_velocity
        self.velocity = (0, 0)
        self.direction = None
        self.damage_types = damage_types

    def copy(self):
        copied_physic = FireBallPhysic((self.collision.rect.w, self.collision.rect.h), self.max_velocity, self.damage_types)
        copied_physic.direction = self.direction
        return copied_physic

    def set_attack_rect(self, start_pos, direction):
        self.collision.rect.topleft = start_pos
        self.direction = direction
        if direction == 0:
            self.velocity = (0, -self.max_velocity)
        elif direction == 90:
            self.velocity = (self.max_velocity, 0)
        elif direction == 180:
            self.velocity = (0, self.max_velocity)
        elif direction == 90:
            self.velocity = (-self.max_velocity, 0)


class FireBallCollision:
    def __init__(self, rect):
        self.rect = rect
        self.collisions_around = {}

    def get_collisions_around(self, collisions_map, tile_size):
        tile_loc = ((self.rect.x + (self.rect.width // 2)) // tile_size[0], (self.rect.y + (self.rect.height // 2)) // tile_size[1])
        for offset_name in NEIGHBOUR_OFFSETS:
            check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size[0]) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size[1])
            if check_lock in collisions_map:
                self.collisions_around[offset_name] = collisions_map[check_lock]

    def update(self, velocity, room, index, movement=(0, 0)):
        for direction in self.collisions_around:
            if self.collisions_around[direction].rect.colliderect(self.rect) and not self.collisions_around[direction].cross_ability:
                del room.collisions_map.movable_damage_map[index]
                return
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        self.rect.x += movement[0]
        self.rect.y += movement[1]