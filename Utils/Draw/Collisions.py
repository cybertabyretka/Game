import pygame as pg

from Models.Entities.BaseEntity import Entity


def draw_collisions_around(surface: pg.Surface, entity: Entity) -> None:
    for direction in entity.physic.collision.collisions_around:
        pg.draw.rect(surface, (255, 0, 0), entity.physic.collision.collisions_around[direction], 1)
