from Views.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, tile_map, surface, tile_size):
        self.collisions_map = CollisionsMap()
        self.view = RoomV(tile_map, tile_size, surface)
