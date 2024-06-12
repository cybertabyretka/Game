from Views.Entity.Inventory.InventoryCell import InventoryCellV

from Models.Item.Item import EmptyItem

from Utils.Singleton import Singleton


class InventoryCell:
    def __init__(self, item, colour_if_selected, colour_if_unselected):
        self.view = InventoryCellV(item.view.icon, colour_if_selected, colour_if_unselected)
        self.is_selected = False


class EmptyInventoryCell(InventoryCell, Singleton):
    def __init__(self, colour_if_selected, colour_if_unselected):
        super().__init__(EmptyItem(), colour_if_selected, colour_if_unselected)