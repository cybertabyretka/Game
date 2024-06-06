from Views.Game.MainMenu import MainMenuV

from Controllers.Game.MainMenu.MainMenuStates import StartState

from Utils.Stack import Stack


class MainMenu:
    def __init__(self, surface, surface_size, background_rect, buttons):
        self.view = MainMenuV(surface, surface_size, background_rect)
        self.buttons = buttons
        self.states_stack = Stack(StartState(self))