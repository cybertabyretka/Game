from BaseVariables.Buttons.Buttons import *
from BaseVariables.Saves.Saves import AUTO_SAVES, SAVES

from Controllers.Game.Processes.MainMenuProcess import MainMenuProcess
from Controllers.Game.States.MainMenuStates import StartState

from DataStructures.Stack import Stack

from Views.AppStates.MainMenu import MainMenuV


class MainMenu:
    def __init__(self, display, background_surface, entities_surface, rooms_surface):
        self.buttons = {'start_state_buttons': [MAIN_MENU_START_BUTTON, MAIN_MENU_EXIT_BUTTON],
                        'save_selection_state_buttons': [FIRST_SAVE_BUTTON, SECOND_SAVE_BUTTON, THIRD_SAVE_BUTTON, FOURTH_SAVE_BUTTON, FIFTH_SAVE_BUTTON,
                                                         FIRST_AUTO_SAVE_BUTTON, SECOND_AUTO_SAVE_BUTTON, THIRD_AUTO_SAVE_BUTTON, FOURTH_AUTO_SAVE_BUTTON, FIFTH_AUTO_SAVE_BUTTON,
                                                         CANSEL_BUTTON, NEW_GAME_BUTTON]}
        self.view = MainMenuV(display, background_surface)
        self.states_stack = Stack(StartState(self, self.buttons['start_state_buttons']))
        self.process = MainMenuProcess(self)
        self.auto_saves = AUTO_SAVES
        self.saves = SAVES
        self.entities_surface = entities_surface
        self.rooms_surface = rooms_surface