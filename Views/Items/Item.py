import pygame as pg

from Views.Items.ItemIcon import Icon


class ItemV:
    def __init__(self, icon: Icon):
        self.icon: Icon = icon

    def download_images(self) -> None:
        self.icon.download_images()

    def draw(self, surface: pg.Surface, start_pos: tuple[int, int]) -> None:
        self.icon.draw(surface, start_pos)
