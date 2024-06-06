from Utils.Stack import Stack
from Models.Asset import BACKGROUND_PICTURE

from Models.Game.MainMenu import MainMenu


class MainProcess:
    def __init__(self, display):
        background_surface = BACKGROUND_PICTURE
        buttons =
        self.states_stack = Stack(MainMenu(display, background_surface))
