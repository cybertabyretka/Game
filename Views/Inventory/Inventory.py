import pygame as pg

from Models.Inventory.InventoryCell import InventoryCell


class InventoryV:
    def __init__(self, tile_size: tuple[int, int]):
        self.tile_size: tuple[int, int] = tile_size

    @staticmethod
    def download_images(cells: list[list[InventoryCell]]) -> None:
        for i in range(len(cells[0])):
            for j in range(len(cells)):
                cells[i][j].item.view.icon.download_images()

    def draw(self, surface: pg.Surface, cells: list[list[InventoryCell]], start_pos: tuple[int, int]) -> None:
        for i in range(len(cells[0])):
            for j in range(len(cells)):
                cells[i][j].view.draw(surface, (start_pos[0] + (i * self.tile_size[0]), start_pos[1] + (j * self.tile_size[1])), cells[i][j].item.view.icon, cells[i][j].is_selected)
