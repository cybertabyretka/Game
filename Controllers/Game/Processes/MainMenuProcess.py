import pygame as pg

from Controllers.Game.Processes.MainProcess import MainProcess

from DataStructures.Stack import Stack


class MainMenuProcess:
    def __init__(self, main_menu):
        self.main_menu = main_menu

    def do(self, models_stack: Stack, main_process: MainProcess) -> None:
        for event in pg.event.get():
            self.main_menu.states_stack.peek().handle_input(event, models_stack, main_process)
        self.main_menu.states_stack.peek().draw()
