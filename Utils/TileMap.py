from random import randint

from Models.Room.TileMap import TileMap
from Models.Room.Tile import Tile

from Utils.CoordinatesConverter import convert_to_string


def create_base_tile_map(width, height, tile_size):
    tile_map = TileMap()
    for i in range(0, height, tile_size[0]):
        for j in range(0, width, tile_size[1]):
            variant = randint(0, 1)
            if j == 0 or j == height - tile_size[1]:
                tile_map.tile_map[f'{j};{i}'] = Tile(None, 0, (j, i), 'side_wall', variant)
            elif i == 0 or i == width - tile_size[0]:
                tile_map.tile_map[f'{j};{i}'] = Tile(None, 0, (j, i), 'front_wall', variant)
            else:
                tile_map.tile_map[f'{j};{i}'] = Tile(None, 1, (j, i), 'floor', variant)
    variant = randint(0, 1)
    tile_map.tile_map['350;350'] = Tile(None, 0, (350, 350), 'front_wall', variant)
    tile_map.tile_map['385;385'] = Tile(None, 0, (385, 385), 'front_wall', variant)
    return tile_map


def restore_tile_map(tile_map, assets):
    for coord in tile_map:
        tile_map[coord].view.image = assets.base_map_asset[tile_map[coord].type][tile_map[coord].variant]
