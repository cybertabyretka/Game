from Utils.TileMap import create_base_tile_map
from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, TILE_SIZE
from Utils.CoordinatesConverter import convert_to_string

from Models.Asset import TilesAssets
from Models.Room.Room import Room


def make_room(rooms_map, pos, surface, NPCs, player_start_pos, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, tile_size=TILE_SIZE, assets=None, tile_map=None):
    if assets is None:
        assets = TilesAssets()
    if tile_map is None:
        tile_map = create_base_tile_map(width, height, tile_size, assets)
    room = Room(player_start_pos, tile_map, surface, tile_size, NPCs)
    room.view.tile_map = tile_map
    room.collisions_map.get_map_from_object(room.view.tile_map.tile_map)
    room.collisions_map.get_graph()
    rooms_map[pos[0]][pos[1]] = room


def connect_rooms(door):
    add_doors(door)
    door.current_room.collisions_map.get_map_from_object(door.current_room.view.tile_map.tile_map)
    door.current_room.collisions_map.get_graph()
    door.next_room.collisions_map.get_map_from_object(door.next_room.view.tile_map.tile_map)
    door.next_room.collisions_map.get_graph()


def add_doors(door):
    current_str_coordinates = convert_to_string(door.current_tile.collision.rect.topleft)
    next_str_coordinates = convert_to_string(door.next_tile.collision.rect.topleft)
    door.current_room.collisions_map.doors.append(door)
    door.current_room.view.tile_map.tile_map[current_str_coordinates] = door.current_tile
    door.current_room.collisions_map.map[current_str_coordinates] = door.current_tile.collision
    door.next_room.collisions_map.doors.append(door)
    door.next_room.view.tile_map.tile_map[next_str_coordinates] = door.next_tile
    door.next_room.collisions_map.map[next_str_coordinates] = door.next_tile.collision