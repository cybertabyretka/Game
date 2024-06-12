class GameState:
    def __init__(self, game):
        self.game = game
        self.finished = True

    def handle_input(self, event, processes_stack, main_process):
        pass

    def update(self):
        pass

    def draw(self):
        pass


class MainMenuState:
    def __init__(self, main_menu, game):
        self.main_menu = main_menu
        self.game = game
        self.finished = True

    def handle_input(self, event, processes_stack, main_process):
        pass

    def update(self):
        pass

    def draw(self):
        pass