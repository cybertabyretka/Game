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
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['side_wall'][variant - 1], 'side_wall', variant, 0., (float(j), float(i)))
            elif i == 0 or i == width - tile_size[0]:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 'front_wall', variant, 0., (float(j), float(i)))
            else:
                tile_map.tile_map[f'{j};{i}'] = Tile(assets.base_map_asset['floor'][variant - 1], 'floor', variant, 1., (float(j), float(i)))
    variant = randint(1, 2)
    tile_map.tile_map['350;350'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 'front_wall', variant, 0, (350, 350))
    tile_map.tile_map['385;385'] = Tile(assets.base_map_asset['front_wall'][variant - 1], 'front_wall', variant, 0, (385, 385))
    return tile_map


def add_doors(door):
    current_str_coordinates = convert_to_string(door.current_tile.collision.rect.topleft)
    next_str_coordinates = convert_to_string(door.next_tile.collision.rect.topleft)
    door.current_room.collisions_map.doors.append(door)
    door.current_room.view.tile_map.tile_map[current_str_coordinates] = door.current_tile
    door.current_room.collisions_map.map[current_str_coordinates] = door.current_tile.collision
    door.next_room.collisions_map.doors.append(door)
    door.next_room.view.tile_map.tile_map[next_str_coordinates] = door.next_tile
    door.next_room.collisions_map.map[next_str_coordinates] = door.next_tile.collision

