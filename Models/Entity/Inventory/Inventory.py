from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import EmptyInventoryCell

from Utils.Setting import WHITE_RGB, GRAY_RGB


class Inventory:
    def __init__(self, size, tile_size, start_pos):
        self.view = InventoryV(tile_size, start_pos)
        self.cells = [[EmptyInventoryCell(GRAY_RGB, WHITE_RGB) for _ in range(size[0])] for _ in range(size[1])]