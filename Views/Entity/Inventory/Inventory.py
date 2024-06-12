class InventoryV:
    def __init__(self, tile_size, start_pos):
        self.tile_size = tile_size
        self.start_pos = start_pos

    def draw(self, surface, items):
        for i in range(len(items[0])):
            for j in range(len(items)):
                pass
