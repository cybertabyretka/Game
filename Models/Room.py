from Views.Room import RoomV
from Models.TileMaps import TileMap


class Room:
    def __init__(self, width, height, assets, pos=(0., 0.)):
        self.width = width
        self.height = height
        self.tile_map = TileMap(assets)
        self.room_view = RoomV((width, height), pos)