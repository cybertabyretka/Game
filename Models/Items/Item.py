from BaseVariables.Others import EMPTY_NAME, EMPTY_SIZE

from Utils.Singleton import Singleton

from Models.InteractionObjects.Button import Button

from Views.Items.Item import ItemV
from Views.Items.ItemIcon import EmptyIcon, Icon


class Item:
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, buttons: list[Button]):
        self.name: str = name
        self.size: tuple[int, int] = size
        self.view: ItemV = ItemV(icon)
        self.buttons: list[Button] = buttons

    def set_buttons_start_pos(self, start_pos: tuple[int, int]) -> None:
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
        super().__init__(EMPTY_NAME, EMPTY_SIZE, EmptyIcon(), [])

    def copy_for_save(self):
        return EmptyItem()
