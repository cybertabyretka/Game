from random import randint

from Models.Room.TileMap import TileMap
from Models.Room.Tile import Tile

from BaseVariables.PathsAsset import TILES


def create_base_tile_map(width, height, tile_size):
    tile_map = TileMap()
    for i in range(0, height, tile_size[0]):
        for j in range(0, width, tile_size[1]):
            variant = randint(0, 1)
            if j == 0 or j == height - tile_size[1]:
                tile_map.map[f'{j};{i}'] = Tile(f'{TILES["side_wall"]}/{variant}.png', 0, (j, i))
            elif i == 0 or i == width - tile_size[0]:
                tile_map.map[f'{j};{i}'] = Tile(f'{TILES["front_wall"]}/{variant}.png', 0, (j, i))
            else:
                tile_map.map[f'{j};{i}'] = Tile(f'{TILES["floor"]}/{variant}.png', 1, (j, i))
    variant = randint(0, 1)
    tile_map.map['350;350'] = Tile(f'{TILES["front_wall"]}/{variant}.png', 0, (350, 350))
    tile_map.map['385;385'] = Tile(f'{TILES["front_wall"]}/{variant}.png', 0, (385, 385))
    return tile_map
