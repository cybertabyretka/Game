import pygame as pg

from BaseVariables.TileMapOffsets import NEIGHBOUR_OFFSETS
from BaseVariables.Others import TILE_SIZE

from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.Entities.Physic.EntitiesProcess import entities_process
from Controllers.RoomMap.TilePhysic import TileCollision

from Constants.Directions import *

from Models.Entities.BaseEntity import Entity

from Utils.DistanceCounting import manhattan_distance


class BaseEntityCollision:
    def __init__(self, pos: tuple[int, int], size: tuple[int, int]):
        self.rect: pg.Rect = pg.Rect(pos[0], pos[1], size[0], size[1])
        self.collisions_around: dict[str, TileCollision | None] = {}

    def update(self, velocity: list[int], entities: list[Entity], collisions_map: dict[str, TileCollision], movement: tuple[int] = (0, 0)) -> None:
        get_collisions_around(self.rect, TILE_SIZE, collisions_map, self.collisions_around)
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        movement = self.contacts_process(movement)
        movement = self.entities_contacts_process(movement, entities)
        self.rect.x += movement[0]
        self.rect.y += movement[1]

    def right_contacts_process(self, movement: list[int]) -> list[int]:
        if not self.collisions_around[RIGHT].cross_ability and self.collisions_around[RIGHT].rect.y - self.rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around[RIGHT].rect.x - self.rect.topright[0])
        if not self.collisions_around[RIGHT_DOWN].cross_ability and self.collisions_around[RIGHT_DOWN].rect.y - self.rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around[RIGHT_DOWN].rect.x - self.rect.topright[0])
        if not self.collisions_around[RIGHT_UP].cross_ability and self.rect.y - self.collisions_around[RIGHT_UP].rect.y < self.rect.height:
            movement[0] = min(movement[0], self.collisions_around[RIGHT_UP].rect.x - self.rect.topright[0])
        return movement

    def left_contacts_process(self, movement: list[int]) -> list[int]:
        if not self.collisions_around[LEFT].cross_ability and self.collisions_around[LEFT].rect.y - self.rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around[LEFT].rect.topright[0] - self.rect.x)
        if not self.collisions_around[LEFT_DOWN].cross_ability and self.collisions_around[LEFT_DOWN].rect.y - self.rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around[LEFT_DOWN].rect.topright[0] - self.rect.x)
        if not self.collisions_around[LEFT_UP].cross_ability and self.rect.y - self.collisions_around[LEFT_UP].rect.y < self.rect.height:
            movement[0] = max(movement[0], self.collisions_around[LEFT_UP].rect.topright[0] - self.rect.x)
        return movement

    def up_contacts_process(self, movement: list[int]) -> list[int]:
        if not self.collisions_around[UP].cross_ability and self.collisions_around[UP].rect.x - self.rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around[UP].rect.bottomleft[1] - self.rect.y)
        if not self.collisions_around[RIGHT_UP].cross_ability and self.collisions_around[RIGHT_UP].rect.x - self.rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around[RIGHT_UP].rect.bottomleft[1] - self.rect.y)
        if not self.collisions_around[LEFT_UP].cross_ability and self.rect.x - self.collisions_around[LEFT_UP].rect.x < self.rect.width:
            movement[1] = max(movement[1], self.collisions_around[LEFT_UP].rect.bottomleft[1] - self.rect.y)
        return movement

    def down_contacts_process(self, movement: list[int]) -> list[int]:
        if not self.collisions_around[DOWN].cross_ability and self.collisions_around[DOWN].rect.x - self.rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around[DOWN].rect.y - self.rect.bottomleft[1])
        if not self.collisions_around[RIGHT_DOWN].cross_ability and self.collisions_around[RIGHT_DOWN].rect.x - self.rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around[RIGHT_DOWN].rect.y - self.rect.bottomleft[1])
        if not self.collisions_around[LEFT_DOWN].cross_ability and self.rect.x - self.collisions_around[LEFT_DOWN].rect.x < self.rect.width:
            movement[1] = min(movement[1], self.collisions_around[LEFT_DOWN].rect.y - self.rect.bottomleft[1])
        return movement

    def entities_contacts_process(self, movement: list[int], entities: list[Entity]) -> list[int]:
        for entity in entities:
            if entity.health.health > 0 and entity.physic.collision is not self and manhattan_distance((entity.physic.collision.rect.x, entity.physic.collision.rect.y), (self.rect.x, self.rect.y)) <= max(self.rect.width, self.rect.height) * 2:
                entities_process(movement, entity.physic.collision.rect, self.rect)
        return movement

    def contacts_process(self, movement: list[int]) -> list[int]:
        if movement[0] > 0:
            movement = self.right_contacts_process(movement)
        if movement[0] < 0:
            movement = self.left_contacts_process(movement)
        if movement[1] < 0:
            movement = self.up_contacts_process(movement)
        if movement[1] > 0:
            movement = self.down_contacts_process(movement)
        return movement


class BaseEntityPhysic:
    def __init__(self, width: int, height: int, start_pos: tuple[int, int], max_velocity: int, collision_type: type[BaseEntityCollision]):
        self.collision: BaseEntityCollision = collision_type(start_pos, (width, height))
        self.max_velocity: int = max_velocity
        self.velocity: list[int] = [0, 0]
