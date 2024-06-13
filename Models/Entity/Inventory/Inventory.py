from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import InventoryCell
from Models.Item.Item import EmptyItem

from Utils.Setting import GRAY_RGB, GREEN_RGB


class Inventory:
    def __init__(self, size, tile_size):
        self.size = size
        self.view = InventoryV(tile_size)
        self.cells = [[InventoryCell(EmptyItem(), GREEN_RGB, GRAY_RGB) for _ in range(size[0])] for _ in range(size[1])]

    def change_cell_state(self, index):
        self.cells[index[0]][index[1]].is_selected = not self.cells[index[0]][index[1]].is_selected

    def place_item(self, index, item):
        self.cells[index[0]][index[1]].item = item

    def place_items(self, index, items):
        for i in range(len(index)):
            self.place_item(index[i], items[i])

    def switch_items(self, index1, index2):
        temp = self.cells[index1[0]][index1[1]].item
        self.place_item(index1, self.cells[index2[0]][index2[1]].item)
        self.place_item(index2, temp)