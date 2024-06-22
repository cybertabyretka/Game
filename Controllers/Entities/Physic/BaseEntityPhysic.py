import pygame as pg

from BaseVariables.TileMapOffsets import NEIGHBOUR_OFFSETS

from Utils.DistanceCounting import manhattan_distance


class BaseEntityPhysics:
    def __init__(self, width, height, start_pos, max_velocity, collision_type):
        self.collision = collision_type(start_pos, (width, height))
        self.max_velocity: int = max_velocity
        self.velocity: list[int] = [0, 0]


class BaseEntityCollision:
    def __init__(self, pos, size):
        self.rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.collisions_around = {}

    def get_collisions_around(self, collisions_map, tile_size):
        tile_loc = ((self.rect.x + (self.rect.width // 2)) // tile_size[0], (self.rect.y + (self.rect.height // 2)) // tile_size[1])
        for offset_name in NEIGHBOUR_OFFSETS:
            check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size[0]) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size[1])
            if check_lock in collisions_map:
                self.collisions_around[offset_name] = collisions_map[check_lock]

    def update(self, velocity, entities, movement=(0, 0)):
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        if (movement[0] != 0 and movement[1] == 0) or (movement[0] == 0 and movement[1] != 0):
            movement = self.straight_contacts_process(movement)
        elif movement[0] != 0 and movement[1] != 0:
            movement = self.corner_contacts_process(movement)
        movement = self.entities_contacts_process(movement, entities)
        self.rect.x += movement[0]
        self.rect.y += movement[1]

    def entities_contacts_process(self, movement, entities):
        for entity in entities:
            if entity.health.health > 0 and entity.physic.collision is not self and manhattan_distance((entity.physic.collision.rect.x, entity.physic.collision.rect.y), (self.rect.x, self.rect.y)) <= max(self.rect.width, self.rect.height) * 2:
                if movement[0] > 0 and (entity.physic.collision.rect.x - self.rect.topright[0]) >= 0 and abs(self.rect.y - entity.physic.collision.rect.y) <= self.rect.height:
                    movement[0] = min(movement[0], entity.physic.collision.rect.x - self.rect.topright[0])
                if movement[0] < 0 and (entity.physic.collision.rect.topright[0] - self.rect.x) <= 0 and abs(self.rect.y - entity.physic.collision.rect.y) <= self.rect.height:
                    movement[0] = max(movement[0], entity.physic.collision.rect.topright[0] - self.rect.x)
                if movement[1] > 0 and (entity.physic.collision.rect.y - self.rect.bottomleft[1]) >= 0 and abs(self.rect.x - entity.physic.collision.rect.x) <= self.rect.width:
                    movement[1] = min(movement[1], entity.physic.collision.rect.y - self.rect.bottomleft[1])
                if movement[1] < 0 and (entity.physic.collision.rect.bottomleft[1] - self.rect.y) <= 0 and abs(self.rect.x - entity.physic.collision.rect.x) <= self.rect.width:
                    movement[1] = max(movement[1], entity.physic.collision.rect.bottomleft[1] - self.rect.y)
        return movement

    def right_contacts_process(self, movement):
        if not self.collisions_around['right'].cross_ability and self.collisions_around['right'].rect.y - self.rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around['right'].rect.x - self.rect.topright[0])
        if not self.collisions_around['right_down'].cross_ability and self.collisions_around['right_down'].rect.y - self.rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around['right_down'].rect.x - self.rect.topright[0])
        if not self.collisions_around['right_up'].cross_ability and self.rect.y - self.collisions_around['right_up'].rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around['right_up'].rect.x - self.rect.topright[0])
        return movement

    def left_contacts_process(self, movement):
        if not self.collisions_around['left'].cross_ability and self.collisions_around['left'].rect.y - self.rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around['left'].rect.topright[0] - self.rect.x)
        if not self.collisions_around['left_down'].cross_ability and self.collisions_around['left_down'].rect.y - self.rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around['left_down'].rect.topright[0] - self.rect.x)
        if not self.collisions_around['left_up'].cross_ability and self.rect.y - self.collisions_around['left_up'].rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around['left_up'].rect.topright[0] - self.rect.x)
        return movement

    def up_contacts_process(self, movement):
        if not self.collisions_around['up'].cross_ability and self.collisions_around['up'].rect.x - self.rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around['up'].rect.bottomleft[1] - self.rect.y)
        if not self.collisions_around['right_up'].cross_ability and self.collisions_around['right_up'].rect.x - self.rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around['right_up'].rect.bottomleft[1] - self.rect.y)
        if not self.collisions_around['left_up'].cross_ability and self.rect.x - self.collisions_around['left_up'].rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around['left_up'].rect.bottomleft[1] - self.rect.y)
        return movement

    def down_contacts_process(self, movement):
        if not self.collisions_around['down'].cross_ability and self.collisions_around['down'].rect.x - self.rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around['down'].rect.y - self.rect.bottomleft[1])
        if not self.collisions_around['right_down'].cross_ability and self.collisions_around['right_down'].rect.x - self.rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around['right_down'].rect.y - self.rect.bottomleft[1])
        if not self.collisions_around['left_down'].cross_ability and self.rect.x - self.collisions_around['left_down'].rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around['left_down'].rect.y - self.rect.bottomleft[1])
        return movement

    def corner_contacts_process(self, movement):
        if movement[0] > 0 and movement[1] > 0:
            movement = self.right_contacts_process(movement)
            movement = self.down_contacts_process(movement)
        elif movement[0] > 0 > movement[1]:
            movement = self.right_contacts_process(movement)
            movement = self.up_contacts_process(movement)
        elif movement[0] < 0 < movement[1]:
            movement = self.left_contacts_process(movement)
            movement = self.down_contacts_process(movement)
        else:
            movement = self.left_contacts_process(movement)
            movement = self.up_contacts_process(movement)
        return movement

    def straight_contacts_process(self, movement):
        if movement[0] > 0:
            movement = self.right_contacts_process(movement)
        elif movement[0] < 0:
            movement = self.left_contacts_process(movement)
        elif movement[1] < 0:
            movement = self.up_contacts_process(movement)
        else:
            movement = self.down_contacts_process(movement)
        return movement
