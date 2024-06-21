import pygame as pg


class InventoryCellV:
    def __init__(self, colour_if_selected, color_if_unselected):
        self.colour_if_selected = colour_if_selected
        self.colour_if_unselected = color_if_unselected

    def draw(self, surface, start_pos, icon, is_selected):
        if is_selected:
            pg.draw.rect(surface, self.colour_if_selected, (start_pos, (icon.image.get_rect().width, icon.image.get_rect().height)))
        else:
            pg.draw.rect(surface, self.colour_if_unselected, (start_pos, (icon.image.get_rect().width, icon.image.get_rect().height)))
        icon.draw(surface, start_pos)
