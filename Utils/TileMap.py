from random import randint
from Models.TileMap import TileMap
from Models.Tile import Tile


def create_base_tile_map(width, height, tile_size, assets):
    tile_map = TileMap(assets)
    for i in range(0, height, tile_size[0]):
        for j in range(0, width, tile_size[1]):
            variant = randint(1, 2)
            if j == 0 or j == height - tile_size[1]:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_asset['front_wall'][variant-1], 'front_wall', variant, 0., (float(j), float(i)))
            elif i == 0 or i == width - tile_size[0]:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_asset['side_wall'][variant-1], 'side_wall', variant, 0., (float(j), float(i)))
            else:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_asset['floor'][variant-1], 'floor', variant, 1., (float(j), float(i)))
    variant = randint(1, 2)
    tile_map.tile_map['350;350'] = Tile(assets.base_asset['front_wall'][variant-1], 'front_wall', variant, 0, (350, 350))
    tile_map.tile_map['385;385'] = Tile(assets.base_asset['front_wall'][variant - 1], 'front_wall', variant, 0, (385, 385))
    return tile_map
