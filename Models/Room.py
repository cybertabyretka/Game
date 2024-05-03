from Views.Room import RoomV


class Room:
    def __init__(self, width, height, tile_map, pos=(0., 0.)):
        self.width = width
        self.height = height
        self.room_view = RoomV(tile_map, pos)