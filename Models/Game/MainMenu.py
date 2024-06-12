from Views.Game.MainMenu import MainMenuV

from Controllers.Game.MainMenuStates import StartState
from Controllers.Processes.MainMenuProcess import MainMenuProcess

from Utils.Stack import Stack
from Utils.Setting import WHITE_RGB, GRAY_RGB, FONT_PATH

from Models.Button import make_button


class MainMenu:
    def __init__(self, display, background_surface, game):
        self.buttons = [make_button(300, 300, 100, 50, 1, GRAY_RGB, WHITE_RGB, 'Start', WHITE_RGB, 20, FONT_PATH),
                        make_button(300, 350, 100, 50, 1, GRAY_RGB, WHITE_RGB, 'Exit', WHITE_RGB, 20, FONT_PATH)]
        self.view = MainMenuV(display, background_surface)
        self.states_stack = Stack(StartState(self, game))
        self.process = MainMenuProcess(self)