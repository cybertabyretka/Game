from Utils.TileMap import create_base_tile_map, add_doors
from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, TILE_SIZE

from Models.Asset import TilesAssets
from Models.Room.Room import Room


class RoomsMap:
    def __init__(self, size):
        self.map = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.current_index = (0, 0)

    # noinspection PyTypeChecker
    def make_room(self, pos, surface, NPCs, player_start_pos, width=DISPLAY_WIDTH, height=DISPLAY_HEIGHT, tile_size=TILE_SIZE, assets=None, tile_map=None):
        if assets is None:
            assets = TilesAssets()
        if tile_map is None:
            tile_map = create_base_tile_map(width, height, tile_size, assets)
        room = Room(player_start_pos, tile_map, surface, tile_size, NPCs)
        room.view.tile_map = tile_map
        room.collisions_map.get_map_from_object(room.view.tile_map.tile_map)
        room.collisions_map.get_graph()
        self.map[pos[0]][pos[1]] = room

    @staticmethod
    def connect_rooms(door):
        add_doors(door)
        door.current_room.collisions_map.get_map_from_object(door.current_room.view.tile_map.tile_map)
        door.current_room.collisions_map.get_graph()
        door.next_room.collisions_map.get_map_from_object(door.next_room.view.tile_map.tile_map)
        door.next_room.collisions_map.get_graph()

    def get_current_room(self):
        return self.map[self.current_index[0]][self.current_index[1]]

    def render_current_room(self, surface):
        self.get_current_room().render_tile_map(surface)
