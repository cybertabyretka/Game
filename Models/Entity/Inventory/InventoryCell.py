from Views.Entity.Inventory.InventoryCell import InventoryCellV

from Models.Item.Item import EmptyItem

from Utils.Singleton import Singleton


class InventoryCell:
    def __init__(self, item, colour_if_selected, colour_if_unselected):
        self.view = InventoryCellV(colour_if_selected, colour_if_unselected)
        self.item = item
        self.is_selected = False
