import pygame as pg


def draw_collisions_around(surface, entity):
    for direction in entity.physic.collision.collisions_around:
        pg.draw.rect(surface, (255, 0, 0), entity.physic.collision.collisions_around[direction], 1)