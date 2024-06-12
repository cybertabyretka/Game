from Views.Entity.Inventory import InventoryV
from Views.Item.ItemIcon import EmptyIcon


class Inventory:
    def __init__(self, size, tile_size, start_pos):
        self.view = InventoryV(tile_size, start_pos)
        self.items = [[EmptyIcon(tile_size, (i * tile_size[0], j * tile_size[j])) for i in range(size[0])] for j in range(size[1])]