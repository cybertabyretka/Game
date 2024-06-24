from BaseVariables.Surfaces import DISPLAY_WIDTH, DISPLAY_HEIGHT
from BaseVariables.Others import TILE_SIZE

from Controllers.RoomMap.CreateTileMap import create_base_tile_map

from Models.Room.Room import Room
from Models.Entities.NPCs.BaseNPC import NPC
from Models.Room.Tile import LootTile, Tile
from Models.Room.TileMap import TileMap
from Models.Room.Door import Door

from Utils.CoordinatesConverter import convert_to_string


def make_room(rooms_map: list[list[Room | None]], pos: tuple[int, int], NPCs: list[NPC], loot_tiles: list[LootTile], width: int = DISPLAY_WIDTH, height: int = DISPLAY_HEIGHT, tile_size: tuple[int, int] = TILE_SIZE, tile_map: TileMap | None = None) -> None:
    if tile_map is None:
        tile_map = create_base_tile_map(width, height, tile_size)
    room = Room(tile_map, tile_size, NPCs, loot_tiles)
    room.view.tile_map = tile_map
    room.collisions_map.get_map_from_object(room.view.tile_map.map)
    room.collisions_map.get_graph()
    rooms_map[pos[0]][pos[1]] = room


def create_tile_map(tiles: list[Tile], width: int = DISPLAY_WIDTH, height: int = DISPLAY_HEIGHT, tile_size: tuple[int, int] = TILE_SIZE):
    tile_map = create_base_tile_map(width, height, tile_size)
    for tile in tiles:
        tile_map.map[convert_to_string((tile.collision.rect.x, tile.collision.rect.y))] = tile
    return tile_map


def connect_rooms(doors: list[Door]) -> None:
    for door in doors:
        add_doors(door)
        door.current_room.collisions_map.get_map_from_object(door.current_room.view.tile_map.map)
        door.current_room.collisions_map.get_graph()
        door.next_room.collisions_map.get_map_from_object(door.next_room.view.tile_map.map)
        door.next_room.collisions_map.get_graph()


def add_doors(door: Door) -> None:
    current_str_coordinates = convert_to_string(door.current_tile.collision.rect.topleft)
    next_str_coordinates = convert_to_string(door.next_tile.collision.rect.topleft)
    door.current_room.collisions_map.doors.append(door)
    door.current_room.view.tile_map.map[current_str_coordinates] = door.current_tile
    door.current_room.collisions_map.map[current_str_coordinates] = door.current_tile.collision
    door.next_room.collisions_map.doors.append(door)
    door.next_room.view.tile_map.map[next_str_coordinates] = door.next_tile
    door.next_room.collisions_map.map[next_str_coordinates] = door.next_tile.collision