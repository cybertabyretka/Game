from Models.Item.Item import Item


class Shield(Item):
    def __init__(self, name, size, icon, strength, damage_types, buttons):
        super().__init__(name, size, icon, buttons)
        self.strength = strength
        self.damage_types = damage_types

    def copy_for_save(self):
        return Shield(self.name, self.size, self.view.icon.copy_for_save(), self.strength, self.damage_types, self.buttons)
