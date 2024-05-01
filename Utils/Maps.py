from random import randint


def create_base_map(tile_map):
    for i in range(0, tile_map.height, tile_map.tile_size):
        for j in range(0, tile_map.width, tile_map.tile_size):
            if j == 0 or j == 665:
                tile_map.tile_map[f'{i};{j}'] = {'type': 'front_wall', 'variant': randint(1, 2), 'pos': (i, j)}
            elif i == 0 or i == 665:
                tile_map.tile_map[f'{i};{j}'] = {'type': 'side_wall', 'variant': randint(1, 2), 'pos': (i, j)}
            else:
                tile_map.tile_map[f'{i};{j}'] = {'type': 'floor', 'variant': randint(1, 2), 'pos': (i, j)}
