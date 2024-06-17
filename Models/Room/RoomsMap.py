class RoomsMap:
    def __init__(self, size, current_index=(0, 0)):
        self.size = size
        self.map = [[None for _ in range(size[0])] for _ in range(size[1])]
        self.current_index = current_index

    def get_current_room(self):
        return self.map[self.current_index[0]][self.current_index[1]]

    def copy_for_save(self, current_room):
        copied_map = RoomsMap(self.size)
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if self.map[i][j] is not None:
                    copied_map.map[i][j] = self.map[i][j].copy_for_save()
                    if self.map[i][j] == current_room:
                        copied_map.current_index = (i, j)
        return copied_map

    def download_images(self):
        for i in range(self.size[1]):
            for j in range(self.size[0]):
                if self.map[i][j] is not None:
                    self.map[i][j].download_images()
