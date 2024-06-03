import pygame as pg


def draw(graph, surface):
    for coord in graph:
        lst = graph[coord]
        coord1_int = coord[1].split(';')
        coord1_int = [int(coord1_int[0]) + 17, int(coord1_int[1]) + 17]
        for coord2 in lst:
            coord2_int = coord2[1].split(';')
            coord2_int = [int(coord2_int[0]) + 17, int(coord2_int[1]) + 17]
            pg.draw.line(surface, (255, 0, 0), coord1_int, coord2_int)