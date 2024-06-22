class MainMenuV:
    def __init__(self, display, background_rect):
        self.display = display
        self.background_surface = background_rect

    def draw(self, buttons):
        self.display.surface.blit(self.background_surface, (0., 0.))
        for button in buttons:
            button.view.draw(self.display.surface)