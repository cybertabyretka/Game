from Views.Game.MainMenu import MainMenuV

from Controllers.Game.MainMenuStates import StartState
from Controllers.Processes.MainMenuProcess import MainMenuProcess

from Utils.Settings.DataStructures.Stack import Stack
from Utils.Settings.Buttons import MAIN_MENU_START_BUTTON, MAIN_MENU_EXIT_BUTTON


class MainMenu:
    def __init__(self, display, background_surface, game):
        self.buttons = [MAIN_MENU_START_BUTTON, MAIN_MENU_EXIT_BUTTON]
        self.view = MainMenuV(display, background_surface)
        self.states_stack = Stack(StartState(self, game))
        self.process = MainMenuProcess(self)