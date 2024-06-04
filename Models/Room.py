from Views.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, tile_map, surface, tile_size=35):
        self.collisions_map = CollisionsMap()
        self.room_view = RoomV(tile_map, tile_size, surface)
