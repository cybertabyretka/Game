class Door:
    def __init__(self, current_tile, next_tile, current_start_pos, next_start_pos):
        self.current_tile = current_tile
        self.current_room = None
        self.current_start_pos = current_start_pos
        self.next_tile = next_tile
        self.next_room = None
        self.next_start_pos = next_start_pos

    def add_rooms(self, current_room, next_room):
        self.current_room = current_room
        self.next_room = next_room

    def get_next_room(self, current_room):
        if current_room == self.current_room:
            return self.next_room, self.next_start_pos, True
        return self.current_room, self.current_start_pos, False

    def download_images(self):
        self.current_tile.view.download_images()
        self.next_tile.view.download_images()

    def copy_for_save(self):
        copied_door = Door(self.current_tile.copy_for_save(), self.next_tile.copy_for_save(), self.current_start_pos, self.next_start_pos)
        return copied_door
