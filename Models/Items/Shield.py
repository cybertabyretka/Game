from Models.Items.Item import Item
from Models.InteractionObjects.Button import Button

from Views.Items.ItemIcon import Icon


class Shield(Item):
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, buttons: list[Button], damage_types: dict[str, int]):
        super().__init__(name, size, icon, buttons)
        self.damage_types: dict[str, int] = damage_types

    def copy_for_save(self):
        return Shield(self.name, self.size, self.view.icon.copy_for_save(), self.buttons, self.damage_types)
