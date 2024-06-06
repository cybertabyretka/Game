class MainMenuV:
    def __init__(self, surface, surface_size, background_rect):
        self.surface = surface
        self.surface_size = surface_size
        self.background_rect = background_rect

    def render(self, buttons):
        self.surface.blit(self.background_rect)
        for button in buttons:
            button.view.render(self.surface)