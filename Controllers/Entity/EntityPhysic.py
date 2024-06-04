import pygame as pg
from Utils.Setting import NEIGHBOUR_OFFSETS
from Utils.Graph.PathFinding import manhattan_distance


class EntityPhysics:
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        self.collision = EntityCollision(start_pos, (width, height))
        self.max_velocity: float = max_velocity
        self.velocity: list[float] = [0., 0.]


class EntityCollision:
    def __init__(self, pos, size):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.collisions_around = {}

    def get_collisions_around(self, collisions_map, tile_size):
        tile_loc = (self.rect.x // tile_size, self.rect.y // tile_size)
        for offset_name in NEIGHBOUR_OFFSETS:
            check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size)
            if check_lock in collisions_map:
                self.collisions_around[offset_name] = collisions_map[check_lock]

    def update(self, velocity, entities, movement=(0, 0)):
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        if (movement[0] != 0 and movement[1] == 0) or (movement[0] == 0 and movement[1] != 0):
            movement = self.straight_contacts_process(movement)
        elif movement[0] != 0 and movement[1] != 0:
            movement = self.corner_contacts_process(movement)
        movement, entities_around = self.entities_contacts_process(movement, entities)
        self.rect.x += movement[0]
        self.rect.y += movement[1]
        return entities_around

    def entities_contacts_process(self, movement, entities):
        entities_around = {'right': None, 'left': None, 'down': None, 'up': None}
        for entity in entities:
            if entity.physic.collision is not self and manhattan_distance((entity.physic.collision.collisions_around["center"].rect.x, entity.physic.collision.collisions_around["center"].rect.y), (self.rect.x, self.rect.y)) <= max(self.rect.width, self.rect.height) * 4:
                if movement[0] > 0:
                    if self.rect.topright[0] == entity.physic.collision.rect.x and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
                        movement[0] = 0
                        entities_around['right'] = entity
                if movement[0] < 0:
                    if self.rect.x == entity.physic.collision.rect.topright[0] and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
                        movement[0] = 0
                        entities_around['left'] = entity
                if movement[1] > 0:
                    if self.rect.bottomright[1] == entity.physic.collision.rect.y and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                        movement[1] = 0
                        entities_around['down'] = entity
                if movement[1] < 0:
                    if self.rect.y == entity.physic.collision.rect.bottomright[1] and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                        movement[1] = 0
                        entities_around['up'] = entity
        return movement, entities_around

    def right_contacts_process(self, movement):
        minimum = None
        if self.collisions_around['right'].rect.x - self.rect.topright[0] == 0:
            minimum = self.collisions_around['right'].cross_ability
        if self.collisions_around['right_down'].rect.x - self.rect.topright[0] == 0 and self.collisions_around['right_down'].rect.y - self.rect.bottomright[1] < 0:
            minimum = self.collisions_around['right_down'].cross_ability if minimum is None else min(minimum, self.collisions_around['right_down'].cross_ability)
        if minimum is not None:
            movement[0] *= minimum
        return movement, minimum

    def left_contacts_process(self, movement):
        minimum = None
        if self.rect.x - self.collisions_around['left'].rect.topright[0] == 0:
            minimum = self.collisions_around['left'].cross_ability
        if self.rect.x - self.collisions_around['left_down'].rect.topright[0] == 0 and (self.collisions_around['left_down'].rect.y - self.rect.bottomleft[1] < 0):
            minimum = self.collisions_around['left_down'].cross_ability if minimum is None else min(minimum, self.collisions_around['left_down'].cross_ability)
        if minimum is not None:
            movement[0] *= minimum
        return movement, minimum

    def up_contacts_process(self, movement):
        minimum = None
        if self.rect.y - self.collisions_around['up'].rect.bottomleft[1] == 0:
            minimum = self.collisions_around['up'].cross_ability
        if self.rect.y - self.collisions_around['right_up'].rect.bottomleft[1] == 0 and self.collisions_around['right_up'].rect.x - self.rect.topright[0] < 0:
            minimum = self.collisions_around['right_up'].cross_ability if minimum is None else min(minimum, self.collisions_around['right_up'].cross_ability)
        if minimum is not None:
            movement[1] *= minimum
        return movement, minimum

    def down_contacts_process(self, movement):
        minimum = None
        if self.collisions_around['down'].rect.y - self.rect.bottomleft[1] == 0:
            minimum = self.collisions_around['down'].cross_ability
        if self.collisions_around['right_down'].rect.y - self.rect.bottomleft[1] == 0 and self.collisions_around['right_down'].rect.x - self.rect.bottomright[0] < 0:
            minimum = self.collisions_around['right_down'].cross_ability if minimum is None else min(minimum, self.collisions_around['right_down'].cross_ability)
        if minimum is not None:
            movement[1] *= minimum
        return movement, minimum

    def corner_contacts_process(self, movement):
        if movement[0] > 0 and movement[1] > 0:
            movement, minimum = self.right_contacts_process(movement)
            movement, minimum = self.down_contacts_process(movement)
            if movement[0] > 0 and movement[1] > 0:
                if self.collisions_around['right_down'].rect.y - self.rect.bottomleft[1] == 0 and self.collisions_around['right_down'].rect.x - self.rect.bottomright[0] == 0:
                    minimum = self.collisions_around['right_down'].cross_ability if minimum is None else min(minimum, self.collisions_around['right_down'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        elif movement[0] > 0 > movement[1]:
            movement, minimum = self.right_contacts_process(movement)
            movement, minimum = self.up_contacts_process(movement)
            if movement[0] > 0 > movement[1]:
                if self.collisions_around['right_up'].rect.bottomleft[1] - self.rect.y == 0 and self.collisions_around['right_up'].rect.x - self.rect.topright[0] == 0:
                    minimum = self.collisions_around['right_up'].cross_ability if minimum is None else min(minimum, self.collisions_around['right_up'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        elif movement[0] < 0 < movement[1]:
            movement, minimum = self.left_contacts_process(movement)
            movement, minimum = self.down_contacts_process(movement)
            if movement[0] < 0 < movement[1]:
                if self.collisions_around['left_down'].rect.y - self.rect.bottomleft[1] == 0 and self.rect.x - self.collisions_around['left_down'].rect.topright[0] == 0:
                    minimum = self.collisions_around['left_down'].cross_ability if minimum is None else min(minimum, self.collisions_around['left_down'].cross_ability)
                    movement[0] *= minimum
                    movement[1] *= minimum
        else:
            movement, minimum = self.left_contacts_process(movement)
            movement, minimum = self.up_contacts_process(movement)
            if movement[0] < 0 and movement[1] < 0:
                if self.collisions_around['left_up'].rect.bottomleft[1] - self.rect.y == 0 and self.rect.x - self.collisions_around['left_up'].rect.topright[0] == 0:
                    minimum = self.collisions_around['left_up'].cross_ability if minimum is None else min(minimum, self.collisions_around['left_up'].cross_ability)
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
            movement = self.down_contacts_process(movement)[0]
        return movement


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos=(350., 350.), max_velocity=1):
        super().__init__(width, height, start_pos, max_velocity)
