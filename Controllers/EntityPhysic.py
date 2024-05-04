import pygame as pg
from Utils.Setting import NEIGHBOUR_OFFSETS


class EntityPhysics:
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        self.collision = EntityCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    def contacts_processing(self, movement):
        if movement[0] > 0:
            right = []
            if self.collision.collisions_around['right'].rect.x - (self.collision.rect.x + self.collision.rect.width) == 0:
                right.append(self.collision.collisions_around['right'].cross_ability)
            if self.collision.collisions_around['right_low'].rect.x - (self.collision.rect.x + self.collision.rect.width) == 0 and self.collision.collisions_around['right_low'].rect.y - (self.collision.rect.y + self.collision.rect.height) < 0:
                right.append(self.collision.collisions_around['right_low'].cross_ability)
            if len(right):
                movement[0] *= min(right)
        if movement[0] < 0:
            left = []
            if self.collision.rect.x - (self.collision.collisions_around['left'].rect.x + self.collision.collisions_around['left'].rect.width) == 0:
                left.append(self.collision.collisions_around['left'].cross_ability)
            if self.collision.rect.x - (self.collision.collisions_around['left_low'].rect.x + self.collision.collisions_around['left_low'].rect.width) == 0 and (self.collision.collisions_around['left_low'].rect.y - (self.collision.rect.y + self.collision.rect.height) < 0):
                left.append(self.collision.collisions_around['left_low'].cross_ability)
            if len(left):
                movement[0] *= min(left)
        if movement[1] < 0:
            up = []
            if self.collision.rect.y - (self.collision.collisions_around['up'].rect.y + self.collision.collisions_around['up'].rect.height) == 0:
                up.append(self.collision.collisions_around['up'].cross_ability)
            if self.collision.rect.y - (self.collision.collisions_around['right_up'].rect.y + self.collision.collisions_around['right_up'].rect.height) == 0 and self.collision.collisions_around['right_up'].rect.x - (self.collision.rect.x + self.collision.rect.width) < 0:
                up.append(self.collision.collisions_around['right_up'].cross_ability)
            if len(up):
                movement[1] *= min(up)
        if movement[1] > 0:
            low = []
            if self.collision.collisions_around['low'].rect.y - (self.collision.rect.y + self.collision.rect.height) == 0:
                low.append(self.collision.collisions_around['low'].cross_ability)
            if self.collision.collisions_around['right_low'].rect.y - (self.collision.rect.y + self.collision.rect.height) == 0 and self.collision.collisions_around['right_low'].rect.x - (self.collision.rect.x + self.collision.rect.width) < 0:
                low.append(self.collision.collisions_around['right_low'].cross_ability)
            if len(low):
                movement[1] *= min(low)
        return movement

    def update_collision(self, movement=(0, 0)):
        movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        movement = self.contacts_processing(movement)
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
