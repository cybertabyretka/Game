from Views.Inventory.InventoryCell import InventoryCellV

from Models.Items.Item import Item


class InventoryCell:
    def __init__(self, item: Item, colour_if_selected: tuple[int, int, int], colour_if_unselected: tuple[int, int, int]):
        self.view: InventoryCellV = InventoryCellV(colour_if_selected, colour_if_unselected)
        self.item: Item = item
        self.is_selected: bool = False

    def change_state(self) -> None:
        self.is_selected = not self.is_selected