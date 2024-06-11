class MainMenuV:
    def __init__(self, surface, background_rect):
        self.surface = surface
        self.background_surface = background_rect

    def render(self, buttons):
        self.surface.blit(self.background_surface)
        for button in buttons:
            button.view.render(self.surface)