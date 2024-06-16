from Views.Item.Item import ItemV

from Utils.Singleton import Singleton
from Utils.Setting import EMPTY_NAME, EMPTY_SIZE
from Utils.Settings.Icons.Icons import EMPTY_ICON


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

    def copy_for_save(self):
        return Item(self.name, self.size, self.view.icon.copy_for_save(), self.buttons)


class EmptyItem(Item, Singleton):
    def __init__(self):
        super().__init__(EMPTY_NAME, EMPTY_SIZE, EMPTY_ICON, [])

    def copy_for_save(self):
        return EmptyItem()
