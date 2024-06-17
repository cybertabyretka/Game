class GameState:
    def __init__(self, game):
        self.game = game
        self.finished = False

    def handle_input(self, event, processes_stack, main_process):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class MainMenuState:
    def __init__(self, main_menu, buttons):
        self.buttons = buttons
        self.main_menu = main_menu
        self.finished = False

    def handle_input(self, event, processes_stack, main_process):
        pass

    def update(self):
        pass

    def draw(self):
        pass