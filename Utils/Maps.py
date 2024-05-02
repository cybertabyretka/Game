from random import randint
from Views.Maps import Tile, TileMap


def create_base_map(width, height, tile_size, assets):
    tile_map = TileMap(width, height, tile_size, assets)
    for i in range(0, height, tile_size[0]):
        for j in range(0, width, tile_size[1]):
            variant = randint(1, 2)
            if j == 0 or j == height - tile_size[1]:
                tile_map.tile_map[f'{i};{j}'] = Tile(assets.base_asset['front_wall'][variant-1], 'front_wall', variant)
            elif i == 0 or i == width - tile_size[0]:
                tile_map.tile_map[f'{i};{j}'] = Tile(assets.base_asset['side_wall'][variant-1], 'side_wall', variant)
            else:
                tile_map.tile_map[f'{i};{j}'] = Tile(assets.base_asset['floor'][variant-1], 'floor', variant)
    return tile_map
