class InventoryV:
    def __init__(self, tile_size, start_pos):
        self.tile_size = tile_size
        self.start_pos = start_pos

    def draw(self, surface, cells):
        for i in range(len(cells[0])):
            for j in range(len(cells)):
                cells[i][j].view.draw(surface, (self.start_pos[0] + (i * self.tile_size[0]), self.start_pos[1] + (j * self.tile_size[1])))
