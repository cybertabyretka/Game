class Door:
    def __init__(self, current_tile, next_tile, current_room, next_room, current_start_pos, next_start_pos):
        self.current_tile = current_tile
        self.current_room = current_room
        self.current_start_pos = current_start_pos
        self.next_tile = next_tile
        self.next_room = next_room
        self.next_start_pos = next_start_pos

    def get_next_room(self, current_room):
        if current_room == self.current_room:
            self.current_room, self.next_room = self.next_room, self.current_room
            self.current_tile, self.next_tile = self.next_tile, self.current_tile
            self.current_start_pos, self.next_start_pos = self.next_start_pos, self.current_start_pos
        return self.current_room, self.current_start_pos
