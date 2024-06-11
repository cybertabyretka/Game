from Controllers.Processes.MainProcess import MainProcess


class Main:
    def __init__(self, display, main_menu, game):
        self.process = MainProcess(display)
        self.main_menu = main_menu
        self.game = game