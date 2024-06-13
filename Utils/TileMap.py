from random import randint

from Models.Room.TileMap import TileMap
from Models.Room.Tile import Tile

from Utils.CoordinatesConverter import convert_to_string


def create_base_tile_map(width, height, tile_size, assets):
    tile_map = TileMap(assets)
    for i in range(0, height, tile_size[0]):
        for j in range(0, width, tile_size[1]):
            variant = randint(1, 2)
            if j == 0 or j == height - tile_size[1]:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['side_wall'][variant - 1], 0, (j, i))
            elif i == 0 or i == width - tile_size[0]:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 0, (j, i))
            else:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['floor'][variant - 1], 1, (j, i))
    variant = randint(1, 2)
    tile_map.tile_map['350;350'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 0, (350, 350))
    tile_map.tile_map['385;385'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 0, (385, 385))
    return tile_map
