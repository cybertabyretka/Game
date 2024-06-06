class MainMenuV:
    def __init__(self, display, background_rect):
        self.display = display
        self.background_surface = background_rect

    def render(self, buttons):
        self.display.surface.blit(self.background_surface)
        for button in buttons:
            button.view.render(self.display.surface)