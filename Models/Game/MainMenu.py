from Views.Game.MainMenu import MainMenuV


class MainMenu:
    def __init__(self, surface, surface_size, background_rect, buttons):
        self.view = MainMenuV(surface, surface_size, background_rect)