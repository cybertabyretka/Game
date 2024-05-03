import pygame as pg
from Utils.Setting import NEIGHBOUR_OFFSETS


class EntityPhysics:
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        self.collision = EntityCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    def update_collision(self):
        self.collision.pos[0] += self.velocity[0]
        self.collision.pos[1] += self.velocity[1]
        self.collision.rect[0] += self.velocity[0]
        self.collision.rect[1] += self.velocity[1]


class EntityCollision:
    def __init__(self, pos, size):
        self.pos = list(pos)
        self.size = size
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.collisions_around = {}

    def get_collisions_around(self, collisions_map, tile_size):
        tile_loc = (int(self.pos[0] // tile_size), int(self.pos[1] // tile_size))
        for offset_name in NEIGHBOUR_OFFSETS:
            check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size)
            if check_lock in collisions_map:
                self.collisions_around[offset_name] = collisions_map[check_lock]


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        super().__init__(width, height, start_pos, max_velocity)
