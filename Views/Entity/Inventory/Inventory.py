class InventoryV:
    def __init__(self, tile_size):
        self.tile_size = tile_size

    def draw(self, surface, cells, start_pos):
        for i in range(len(cells[0])):
            for j in range(len(cells)):
                cells[i][j].view.draw(surface, (start_pos[0] + (i * self.tile_size[0]), start_pos[1] + (j * self.tile_size[1])), cells[i][j].item.view.icon, cells[i][j].is_selected)
