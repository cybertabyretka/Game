import pygame as pg

from Views.Items.ItemIcon import Icon


class InventoryCellV:
    def __init__(self, colour_if_selected: tuple[int, int, int], color_if_unselected: tuple[int, int, int]):
        self.colour_if_selected: tuple[int, int, int] = colour_if_selected
        self.colour_if_unselected: tuple[int, int, int] = color_if_unselected

    def draw(self, surface: pg.Surface, start_pos: tuple[int, int], icon: Icon, is_selected: bool) -> None:
        if is_selected:
            pg.draw.rect(surface, self.colour_if_selected, (start_pos, (icon.image.get_rect().width, icon.image.get_rect().height)))
        else:
            pg.draw.rect(surface, self.colour_if_unselected, (start_pos, (icon.image.get_rect().width, icon.image.get_rect().height)))
        icon.draw(surface, start_pos)
