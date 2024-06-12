from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import EmptyInventoryCell

from Utils.Setting import GRAY_RGB, GREEN_RGB


class Inventory:
    def __init__(self, size, tile_size):
        self.view = InventoryV(tile_size)
        self.cells = [[EmptyInventoryCell(GREEN_RGB, GRAY_RGB) for _ in range(size[0])] for _ in range(size[1])]