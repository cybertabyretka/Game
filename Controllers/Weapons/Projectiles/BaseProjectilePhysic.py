import pygame as pg

from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.RoomMap.TilePhysic import TileCollision

from Models.Room.Room import Room

from BaseVariables.Others import TILE_SIZE


class BaseProjectileCollision:
    def __init__(self, rect: pg.Rect):
        self.rect: pg.Rect = rect
        self.collisions_around: dict[str, TileCollision] = {}

    def update(self, velocity: tuple[int, int], room: Room, index: int, movement=(0, 0)) -> None:
        get_collisions_around(self.rect, TILE_SIZE, room.collisions_map.map, self.collisions_around)
        for direction in self.collisions_around:
            if self.collisions_around[direction].rect.colliderect(self.rect) and not self.collisions_around[direction].cross_ability:
                del room.collisions_map.movable_damage_map[index]
                return
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        self.rect.x += movement[0]
        self.rect.y += movement[1]


class BaseProjectilePhysic:
    def __init__(self, size: tuple[int, int], max_velocity: int, damage_types: dict[str, int], collision_type: type[BaseProjectileCollision]):
        self.collision: BaseProjectileCollision = collision_type(pg.Rect((0, 0), size))
        self.max_velocity: int = max_velocity
        self.velocity: tuple[int, int] = (0, 0)
        self.direction: int | None = None
        self.damage_types: dict[str, int] = damage_types

    def copy(self):
        pass

    def set_attack_rect(self, start_pos: tuple[int, int], direction: int) -> None:
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
