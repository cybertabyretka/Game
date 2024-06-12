from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import InventoryCell


class Inventory:
    def __init__(self, size, tile_size, start_pos):
        self.view = InventoryV(tile_size, start_pos)
        self.items = [[InventoryCell() for _ in range(size[0])] for _ in range(size[1])]