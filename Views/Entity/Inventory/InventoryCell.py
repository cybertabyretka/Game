class InventoryCellV:
    def __init__(self, icon, colour_if_selected, color_if_unselected):
        self.icon = icon
        self.colour_if_selected = colour_if_selected
        self.colour_if_unselected = color_if_unselected

    def draw(self, surface, start_pos):
        self.icon.draw(surface, start_pos)