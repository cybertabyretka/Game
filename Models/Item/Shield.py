from Models.Item.Item import Item


class Shield(Item):
    def __init__(self, name, size, icon, strength):
        super().__init__(name, size, icon)
        self.strength = strength
