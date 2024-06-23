import pygame as pg

from BaseVariables.Buttons.Buttons import *
from BaseVariables.Saves.Saves import AUTO_SAVES, SAVES

from Controllers.Game.Processes.MainMenuProcess import MainMenuProcess
from Controllers.Game.States.MainMenuStates import StartState

from DataStructures.Stack import Stack

from Views.AppStates.MainMenu import MainMenuV
from Views.Display import Display

from Models.InteractionObjects.Button import Button
from Models.Save import Save


class MainMenu:
    def __init__(self, display: Display, background_surface: pg.Surface, entities_surface: pg.Surface, rooms_surface: pg.Surface):
        self.buttons: dict[str, list[Button]] = {'start_state_buttons': [MAIN_MENU_START_BUTTON, MAIN_MENU_EXIT_BUTTON],
                                                 'save_selection_state_buttons': [FIRST_SAVE_BUTTON, SECOND_SAVE_BUTTON, THIRD_SAVE_BUTTON, FOURTH_SAVE_BUTTON, FIFTH_SAVE_BUTTON,
                                                                                  FIRST_AUTO_SAVE_BUTTON, SECOND_AUTO_SAVE_BUTTON, THIRD_AUTO_SAVE_BUTTON, FOURTH_AUTO_SAVE_BUTTON, FIFTH_AUTO_SAVE_BUTTON,
                                                                                  CANSEL_BUTTON, NEW_GAME_BUTTON]}
        self.view: MainMenuV = MainMenuV(display, background_surface)
        self.states_stack: Stack = Stack(StartState(self, self.buttons['start_state_buttons']))
        self.process: MainMenuProcess = MainMenuProcess(self)
        self.auto_saves: list[Save] = AUTO_SAVES
        self.saves: list[Save] = SAVES
        self.entities_surface: pg.Surface = entities_surface
        self.rooms_surface: pg.Surface = rooms_surface