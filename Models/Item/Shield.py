from Models.Item.Item import Item


class Shield(Item):
    def __init__(self, name, size, icon, buttons, damage_types):
        super().__init__(name, size, icon, buttons)
        self.damage_types = damage_types

    def copy_for_save(self):
        return Shield(self.name, self.size, self.view.icon.copy_for_save(), self.buttons, self.damage_types)
