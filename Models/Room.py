from Views.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, tile_map, surface, tile_size, NPCs):
        self.collisions_map = CollisionsMap()
        self.view = RoomV(tile_map, tile_size, surface)
        self.NPCs = NPCs
