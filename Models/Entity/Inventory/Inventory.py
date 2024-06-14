from Views.Entity.Inventory.Inventory import InventoryV

from Models.Entity.Inventory.InventoryCell import InventoryCell
from Models.Item.Item import EmptyItem

from Utils.Settings.Colours import GRAY_RGB, GREEN_RGB


class Inventory:
    def __init__(self, size, tile_size):
        self.size = size
        self.view = InventoryV(tile_size)
        self.cells = [[InventoryCell(EmptyItem(), GREEN_RGB, GRAY_RGB) for _ in range(size[0])] for _ in range(size[1])]

    def get_item(self, index):
        return self.cells[index[0]][index[1]]

    def change_cell_state(self, index):
        self.get_item(index).is_selected = not self.get_item(index).is_selected

    def place_item(self, index, item):
        self.get_item(index).item = item

    def place_items(self, index, items):
        for i in range(len(index)):
            self.place_item(index[i], items[i])

    def switch_items(self, index1, index2):
        temp = self.get_item(index1).item
        self.place_item(index1, self.cells[index2[0]][index2[1]].item)
        self.place_item(index2, temp)

    def get_cell_from_pos(self, pos, window):
        inventory_start_pos = (window.view.rect.topleft[0], window.view.rect.topleft[1] + window.view.name.view.font_size)
        inventory_cell_index = list(map(lambda x: x // self.view.tile_size[0], (pos[0] - inventory_start_pos[0], pos[1] - inventory_start_pos[1])))
        return inventory_cell_index

    def switch_with_another_inventory(self, index1, index2, inventory):
        temp = self.get_item(index1).item
        self.get_item(index1).item = inventory.get_item(index2).item
        inventory.get_item(index2).item = temp
