from Views.Game.MainMenu import MainMenuV

from Controllers.Game.MainMenuStates import StartState
from Controllers.Processes.MainMenuProcess import MainMenuProcess

from Utils.Settings.DataStructures.Stack import Stack
from Utils.Settings.Buttons.Buttons import *
from Utils.Settings.Saves.Saves import *


class MainMenu:
    def __init__(self, display, background_surface, game):
        self.buttons = {'start_state_buttons': [MAIN_MENU_START_BUTTON, MAIN_MENU_EXIT_BUTTON],
                        'save_selection_state_buttons': [FIRST_SAVE_BUTTON, SECOND_SAVE_BUTTON, THIRD_SAVE_BUTTON, FOURTH_SAVE_BUTTON, FIFTH_SAVE_BUTTON,
                                                         FIRST_AUTO_SAVE_BUTTON, SECOND_AUTO_SAVE_BUTTON, THIRD_AUTO_SAVE_BUTTON, FOURTH_AUTO_SAVE_BUTTON, FIFTH_AUTO_SAVE_BUTTON]}
        self.view = MainMenuV(display, background_surface)
        self.states_stack = Stack(StartState(self, game, self.buttons['start_state_buttons']))
        self.process = MainMenuProcess(self)
        self.auto_saves = [FIRST_AUTO_SAVE, SECOND_AUTO_SAVE, THIRD_AUTO_SAVE, FOURTH_AUTO_SAVE, FIFTH_AUTO_SAVE]
        self.saves = [FIRST_SAVE, SECOND_SAVE, THIRD_SAVE, FOURTH_SAVE, FIFTH_SAVE]