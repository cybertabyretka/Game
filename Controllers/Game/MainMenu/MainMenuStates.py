from Controllers.Game.BaseStates import MainMenuState


class StartState(MainMenuState):
    def __init__(self, main_menu):
        super().__init__(main_menu)