import pygame as pg
from Utils.Setting import TILE_WITHOUT_COLLISION


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
        self.nearest_collisions = {'up': TILE_WITHOUT_COLLISION, 'up_right': TILE_WITHOUT_COLLISION,
                                   'left': TILE_WITHOUT_COLLISION, 'left_low': TILE_WITHOUT_COLLISION,
                                   'right': TILE_WITHOUT_COLLISION, 'right_low': TILE_WITHOUT_COLLISION,
                                   'low': TILE_WITHOUT_COLLISION, 'low_right': TILE_WITHOUT_COLLISION}

    def set_start_nearest_collisions(self, collisions_map):
        self.set_nearest_straight_collisions(collisions_map)
        self.set_corner_collision('up', 'up_right', 1, collisions_map)
        self.set_corner_collision('low', 'low_right', 1, collisions_map)
        self.set_corner_collision('left', 'left_low', 0, collisions_map)
        self.set_corner_collision('right', 'right_low', 0, collisions_map)

    def set_corner_collision(self, base_name, name, axis, collisions_map):
        if self.pos[axis] + self.size[axis] > self.nearest_collisions[base_name].pos[axis] + self.nearest_collisions[base_name].size[axis]:
            for loc in collisions_map:
                collision = collisions_map[loc]
                int_loc = tuple(map(int, loc.split(';')))
                if self.pos[axis] + self.size[axis] in range(int_loc[axis], int_loc[axis] + collision.size[axis] + 1):
                    self.nearest_collisions[name] = collision
        else:
            self.nearest_collisions[name] = self.nearest_collisions[base_name]

    def set_nearest_straight_collisions(self, collisions_map):
        for loc in collisions_map:
            int_loc = tuple(map(int, loc.split(';')))
            collision = collisions_map[loc]
            tile_width = collision.size[0]
            tile_height = collision.size[1]
            if self.pos[0] in range(int_loc[0], int_loc[0] + tile_width):
                if (int_loc[1] + collisions_map[loc].size[1]) < self.pos[1]:
                    self.nearest_collisions['up'] = collision
                else:
                    if self.nearest_collisions['low'] == TILE_WITHOUT_COLLISION:
                        self.nearest_collisions['low'] = collision
            elif self.pos[1] in range(int_loc[1], int_loc[1] + tile_height):
                if (int_loc[0] + collisions_map[loc].size[0]) < self.pos[1]:
                    self.nearest_collisions['left'] = collision
                else:
                    if self.nearest_collisions['right'] == TILE_WITHOUT_COLLISION:
                        self.nearest_collisions['right'] = collision

    def update_nearest_collisions(self, collisions_map):
        self.set_start_nearest_collisions(collisions_map)


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        super().__init__(width, height, start_pos, max_velocity)
