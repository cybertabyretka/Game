from Views.Display import Display

from Models.AppStates.MainMenu import MainMenu

from Controllers.Game.Processes.MainProcess import MainProcess


class Main:
    def __init__(self, display, main_menu):
        self.process: MainProcess = MainProcess()
        self.display: Display = display
        self.main_menu: MainMenu = main_menu
