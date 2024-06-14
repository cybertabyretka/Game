from Views.Item.Item import ItemV
from Views.Item.ItemIcon import EmptyIcon

from Utils.Singleton import Singleton
from Utils.Setting import EMPTY_NAME, EMPTY_SIZE


class Item:
    def __init__(self, name, size, icon, buttons):
        self.name = name
        self.size = size
        self.view = ItemV(icon)
        self.buttons = buttons

    def set_buttons_start_pos(self, start_pos):
        previous_button_height = 0
        previous_button_y = 0
        for button in self.buttons:
            button.view.rect.topleft = (start_pos[0], max(start_pos[1], previous_button_y) + previous_button_height)
            previous_button_y = button.view.rect.topleft[1]
            previous_button_height = button.view.rect.height


class EmptyItem(Item, Singleton):
    def __init__(self):
        super().__init__(EMPTY_NAME, EMPTY_SIZE, EmptyIcon(), [])
