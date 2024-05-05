import pygame as pg
from Utils.Setting import NEIGHBOUR_OFFSETS


class EntityPhysics:
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        self.collision = EntityCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]

    def right_contacts_process(self, movement):
        minimum = None
        if self.collision.collisions_around['right'].rect.x - self.collision.rect.topright[0] == 0:
            minimum = self.collision.collisions_around['right'].cross_ability
        if self.collision.collisions_around['right_low'].rect.x - self.collision.rect.topright[0] == 0 and self.collision.collisions_around['right_low'].rect.y - self.collision.rect.bottomright[1] < 0:
            minimum = self.collision.collisions_around['right_low'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['right_low'].cross_ability)
        if minimum is not None:
            movement[0] *= minimum
        return movement, minimum

    def left_contacts_process(self, movement):
        minimum = None
        if self.collision.rect.x - self.collision.collisions_around['left'].rect.topright[0] == 0:
            minimum = self.collision.collisions_around['left'].cross_ability
        if self.collision.rect.x - self.collision.collisions_around['left_low'].rect.topright[0] == 0 and (self.collision.collisions_around['left_low'].rect.y - self.collision.rect.bottomleft[1] < 0):
            minimum = self.collision.collisions_around['left_low'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['left_low'].cross_ability)
        if minimum is not None:
            movement[0] *= minimum
        return movement, minimum

    def up_contacts_process(self, movement):
        minimum = None
        if self.collision.rect.y - self.collision.collisions_around['up'].rect.bottomleft[1] == 0:
            minimum = self.collision.collisions_around['up'].cross_ability
        if self.collision.rect.y - self.collision.collisions_around['right_up'].rect.bottomleft[1] == 0 and self.collision.collisions_around['right_up'].rect.x - self.collision.rect.topright[0] < 0:
            minimum = self.collision.collisions_around['right_up'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['right_up'].cross_ability)
        if minimum is not None:
            movement[1] *= minimum
        return movement, minimum

    def low_contacts_process(self, movement):
        minimum = None
        if self.collision.collisions_around['low'].rect.y - self.collision.rect.bottomleft[1] == 0:
            minimum = self.collision.collisions_around['low'].cross_ability
        if self.collision.collisions_around['right_low'].rect.y - self.collision.rect.bottomleft[1] == 0 and self.collision.collisions_around['right_low'].rect.x - self.collision.rect.bottomright[0] < 0:
            minimum = self.collision.collisions_around['right_low'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['right_low'].cross_ability)
        if minimum is not None:
            movement[1] *= minimum
        return movement, minimum

    def corner_contacts_process(self, movement):
        if movement[0] > 0 and movement[1] > 0:
            movement, minimum = self.right_contacts_process(movement)
            movement, minimum = self.low_contacts_process(movement)
            if movement[0] > 0 and movement[1] > 0:
                if self.collision.collisions_around['right_low'].rect.y - self.collision.rect.bottomleft[1] == 0 and self.collision.collisions_around['right_low'].rect.x - self.collision.rect.bottomright[0] == 0:
                    minimum = self.collision.collisions_around['right_low'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['right_low'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        elif movement[0] > 0 > movement[1]:
            movement, minimum = self.right_contacts_process(movement)
            movement, minimum = self.up_contacts_process(movement)
            if movement[0] > 0 > movement[1]:
                if self.collision.collisions_around['right_up'].rect.bottomleft[1] - self.collision.rect.y == 0 and self.collision.collisions_around['right_up'].rect.x - self.collision.rect.topright[0] == 0:
                    minimum = self.collision.collisions_around['right_up'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['right_up'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        elif movement[0] < 0 < movement[1]:
            movement, minimum = self.left_contacts_process(movement)
            movement, minimum = self.low_contacts_process(movement)
            if movement[0] < 0 < movement[1]:
                if self.collision.collisions_around['left_low'].rect.y - self.collision.rect.bottomleft[1] == 0 and self.collision.rect.x - self.collision.collisions_around['left_low'].rect.topright[0] == 0:
                    minimum = self.collision.collisions_around['left_low'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['left_low'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        else:
            movement, minimum = self.left_contacts_process(movement)
            movement, minimum = self.up_contacts_process(movement)
            if movement[0] < 0 and movement[1] < 0:
                if self.collision.collisions_around['left_up'].rect.bottomleft[1] - self.collision.rect.y == 0 and self.collision.rect.x - self.collision.collisions_around['left_up'].rect.topright[0] == 0:
                    minimum = self.collision.collisions_around['left_up'].cross_ability if minimum is None else min(minimum, self.collision.collisions_around['left_up'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        return movement

    def straight_contacts_process(self, movement):
        if movement[0] > 0:
            movement = self.right_contacts_process(movement)[0]
        elif movement[0] < 0:
            movement = self.left_contacts_process(movement)[0]
        elif movement[1] < 0:
            movement = self.up_contacts_process(movement)[0]
        else:
            movement = self.low_contacts_process(movement)[0]
        return movement

    def update_collision(self, movement=(0, 0)):
        movement = [movement[0] + self.velocity[0], movement[1] + self.velocity[1]]
        if (movement[0] != 0 and movement[1] == 0) or (movement[0] == 0 and movement[1] != 0):
            movement = self.straight_contacts_process(movement)
        elif movement[0] != 0 and movement[1] != 0:
            movement = self.corner_contacts_process(movement)
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
