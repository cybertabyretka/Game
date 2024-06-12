class ItemV:
    def __init__(self, icon):
        self.icon = icon

    def draw(self, surface, start_pos):
        self.icon.draw(surface, start_pos)