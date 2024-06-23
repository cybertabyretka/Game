import pygame as pg


def draw_graph(graph: dict[str, list[tuple[int, str]]], surface: pg.Surface) -> None:
    for coord in graph:
        lst = graph[coord]
        coord1_int = coord.split(';')
        coord1_int = [int(coord1_int[0]) + 17, int(coord1_int[1]) + 17]
        for coord2 in lst:
            coord2_int = coord2[1].split(';')
            coord2_int = [int(coord2_int[0]) + 17, int(coord2_int[1]) + 17]
            pg.draw.line(surface, (255, 0, 0), coord1_int, coord2_int)


def draw_way(way: list[tuple[int, int]], surface: pg.Surface) -> None:
    if way:
        start_pos = way[0]
        for pos in way[1:]:
            pg.draw.line(surface, (255, 0, 0), (start_pos[0] + 17, start_pos[1] + 17), (pos[0] + 17, pos[1] + 17))
            start_pos = pos
