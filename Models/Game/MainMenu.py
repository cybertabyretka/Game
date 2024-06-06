from Views.Game.MainMenu import MainMenuV

from Controllers.Game.MainMenu.MainMenuStates import StartState

from Utils.Stack import Stack


class MainMenu:
    def __init__(self, display, background_surface, buttons):
        self.view = MainMenuV(display, background_surface)
        self.buttons = buttons
        self.states_stack = Stack(StartState(self))