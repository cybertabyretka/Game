class RoomsMap:
    def __init__(self, size):
        self.size = size
        self.map = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.current_index = (0, 0)

    def get_current_room(self):
        return self.map[self.current_index[0]][self.current_index[1]]

    def copy_for_save(self):
        copied_map = RoomsMap(self.size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.map[i][j] is not None:
                    copied_map.map[i][j] = self.map[i][j].copy_for_save()
