from Models.Inventory.InventoryCell import InventoryCell


def switch_items(cell1: InventoryCell, cell2: InventoryCell) -> None:
    cell1.item, cell2.item = cell2.item, cell1.item
