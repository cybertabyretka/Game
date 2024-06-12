from Views.Room.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, tile_map, surface, tile_size, NPCs):
        self.live_NPCs_count = len(NPCs)
        self.collisions_map = CollisionsMap()
        self.view = RoomV(tile_map, tile_size, surface)
        self.NPCs = NPCs
