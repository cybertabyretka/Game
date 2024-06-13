from Models.Item.Item import Item


class Shield(Item):
    def __init__(self, name, size, icon, strength, damage_types, buttons):
        super().__init__(name, size, icon, buttons)
        self.strength = strength
        self.damage_types = damage_types
