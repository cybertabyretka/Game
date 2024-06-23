import pygame as pg

from Models.Room.TileMap import TileMap


class RoomV:
    def __init__(self, tile_map: TileMap, tile_size: tuple[int, int]):
        self.tile_map: TileMap = tile_map
        self.tile_size: tuple[int, int] = tile_size

    def render_tile_map(self, surface: pg.Surface) -> None:
        for loc in self.tile_map.map:
            self.tile_map.map[loc].view.draw(surface, tuple(map(int, loc.split(';'))))
