from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import InventoryCell
from Models.Item.Item import EmptyItem

from Utils.Setting import GRAY_RGB, GREEN_RGB


class Inventory:
    def __init__(self, size, tile_size):
        self.view = InventoryV(tile_size)
        self.cells = [[InventoryCell(EmptyItem(), GREEN_RGB, GRAY_RGB) for _ in range(size[0])] for _ in range(size[1])]

    def place_item(self, position, item):
        self.cells[position[0]][position[1]].item = item
        print(self.cells[position[0]][position[1]].item)

    def place_items(self, positions, items):
        for i in range(len(positions)):
            self.place_item(positions[i], items[i])

    def switch_items(self, position1, position2):
        temp = self.cells[position1[0]][position1[1]].item
        self.place_item(position1, self.cells[position2[0]][position2[1]].item)
        self.place_item(position2, temp)