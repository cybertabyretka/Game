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


class EmptyItem(Item, Singleton):
    def __init__(self):
        super().__init__(EMPTY_NAME, EMPTY_SIZE, EmptyIcon(), [])
