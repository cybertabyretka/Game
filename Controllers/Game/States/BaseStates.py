import pygame as pg

from DataStructures.Stack import Stack

from Controllers.Game.Processes.MainProcess import MainProcess

from Models.InteractionObjects.Button import Button


class GameState:
    def __init__(self, game):
        self.game = game
        self.finished: bool = False

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
        pass

    def update(self) -> None:
        pass

    def draw(self) -> None:
        pass


class MainMenuState:
    def __init__(self, main_menu, buttons: list[Button]):
        self.buttons: list[Button] = buttons
        self.main_menu = main_menu
        self.finished: bool = False

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
        pass

    def draw(self) -> None:
        pass
