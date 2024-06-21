from Controllers.RoomMap.MapPhysic import CollisionsMap

from Views.Room.Room import RoomV


class Room:
    def __init__(self, tile_map, tile_size, NPCs, loot_tiles):
        self.loot_tiles = loot_tiles
        self.live_NPCs_count = len(NPCs)
        self.collisions_map = CollisionsMap()
        self.view = RoomV(tile_map, tile_size)
        self.NPCs = NPCs

    def download_images(self):
        for loot_tile in self.loot_tiles:
            loot_tile.download_images()
        for NPC in self.NPCs:
            NPC.view.download_images(NPC.current_weapon, NPC.current_shield, NPC.inventory)
        self.view.tile_map.download_images()

    def copy_for_save(self):
        copied_NPCs = []
        for NPC in self.NPCs:
            copied_NPCs.append(NPC.copy_for_save())
        copied_loot_tiles = []
        for loot_tile in self.loot_tiles:
            copied_loot_tiles.append(loot_tile.copy_for_save())
        copied_room = Room(self.view.tile_map.copy_for_save(), self.view.tile_size, copied_NPCs, copied_loot_tiles)
        copied_room.live_NPCs_count = self.live_NPCs_count
        return copied_room

    def download_map(self):
        self.collisions_map.get_map_from_object(self.view.tile_map.map)
        self.collisions_map.get_graph()