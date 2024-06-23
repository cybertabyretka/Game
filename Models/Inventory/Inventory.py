from Constants.Colours import GRAY_RGB, GREEN_RGB

from Models.Inventory.InventoryCell import InventoryCell
from Models.Items.Item import EmptyItem, Item
from Models.InteractionObjects.InGameWindow import InGameWindow

from Views.Inventory.Inventory import InventoryV


class Inventory:
    def __init__(self, size: tuple[int, int], tile_size: tuple[int, int]):
        self.size: tuple[int, int] = size
        self.view: InventoryV = InventoryV(tile_size)
        self.cells: list[list[InventoryCell]] = [[InventoryCell(EmptyItem(), GREEN_RGB, GRAY_RGB) for _ in range(size[0])] for _ in range(size[1])]

    def get_cell(self, index: tuple[int, int]) -> InventoryCell:
        return self.cells[index[0]][index[1]]

    def copy_for_save(self):
        copied_inventory = Inventory(self.size, self.view.tile_size)
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                copied_inventory.cells[i][j].item = self.cells[i][j].item.copy_for_save()
        return copied_inventory

    def change_cell_state(self, index: tuple[int, int]) -> None:
        self.get_cell(index).change_state()

    def place_item(self, index: tuple[int, int], item: Item) -> None:
        self.get_cell(index).item = item

    def download_images(self) -> None:
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.get_cell((i, j)).item.view.download_images()

    def place_items(self, index: tuple[int, int], items: list[Item]) -> None:
        for i in range(len(index)):
            self.place_item(index[i], items[i])

    def get_cell_index_from_pos(self, pos: tuple[int, int], window: InGameWindow) -> list[int]:
        inventory_start_pos = (window.view.rect.topleft[0], window.view.rect.topleft[1] + window.view.name.view.font_size)
        inventory_cell_index = list(map(lambda x: x // self.view.tile_size[0], (pos[0] - inventory_start_pos[0], pos[1] - inventory_start_pos[1])))
        return inventory_cell_index
