from Controllers.Processes.MainProcess import MainProcess


class Main:
    def __init__(self, display, main_menu):
        self.process = MainProcess(main_menu)
        self.display = display
        self.main_menu = main_menu