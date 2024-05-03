from Views.Room import RoomV
from Controllers.MapPhysic import CollisionsMap


class Room:
    def __init__(self, width, height, tile_map, pos=(0., 0.), tile_size=35):
        self.collisions_map = CollisionsMap()
        self.width = width
        self.height = height
        self.room_view = RoomV(tile_map, pos, tile_size)