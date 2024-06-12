class RoomsMap:
    def __init__(self, size):
        self.map = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.current_index = (0, 0)

    def get_current_room(self):
        return self.map[self.current_index[0]][self.current_index[1]]
