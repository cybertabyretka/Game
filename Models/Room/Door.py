class Door:
    def __init__(self, room_tile1, room_tile2, current_room, next_room):
        self.current_tile = room_tile1
        self.next_tile = room_tile2
        self.current_room = current_room
        self.next_room = next_room

    def get_next_room(self):
        self.current_room, self.next_room = self.next_room, self.current_room
        self.current_tile, self.next_tile = self.next_tile, self.next_tile
        return self.current_room
