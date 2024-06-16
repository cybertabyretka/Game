from Views.Room.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, tile_map, tile_size, NPCs):
        self.live_NPCs_count = len(NPCs)
        self.collisions_map = CollisionsMap()
        self.view = RoomV(tile_map, tile_size)
        self.NPCs = NPCs

    def copy_for_save(self):
        copied_NPCs = []
        for NPC in self.NPCs:
            copied_NPCs.append(NPC.copy_for_save())
        copied_room = Room(self.view.tile_map.copy_for_save(), self.view.tile_size, copied_NPCs)
        copied_room.live_NPCs_count = self.live_NPCs_count
        return copied_room
