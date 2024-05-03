import pygame as pg
from Utils.Setting import NEIGHBOUR_OFFSETS


class EntityPhysics:
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        self.collision = EntityCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    @staticmethod
    def contacts_processing(collision, direction, movement):
        if direction == 'up':
            if movement[1] < 0:
                movement[1] *= collision.cross_ability
        if direction == 'low':
            if movement[1] > 0:
                movement[1] *= collision.cross_ability
        if direction == 'right':
            if movement[0] > 0:
                movement[0] *= collision.cross_ability
        if direction == 'left':
            if movement[0] < 0:
                movement[0] *= collision.cross_ability
        return movement

    def update_collision(self, movement=(0, 0)):
        movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        for direction in self.collision.collisions_around:
            collision = self.collision.collisions_around[direction]
            if self.collision.rect.colliderect(collision.rect) and collision.cross_ability != 1:
                movement = self.contacts_processing(collision, direction, movement)
        self.collision.rect.x += movement[0]
        self.collision.rect.y += movement[1]


class EntityCollision:
    def __init__(self, pos, size):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.collisions_around = {}

    def get_collisions_around(self, collisions_map, tile_size):
        tile_loc = (int(self.rect.x // tile_size), int(self.rect.y // tile_size))
        for offset_name in NEIGHBOUR_OFFSETS:
            check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size)
            if check_lock in collisions_map:
                self.collisions_around[offset_name] = collisions_map[check_lock]


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        super().__init__(width, height, start_pos, max_velocity)
