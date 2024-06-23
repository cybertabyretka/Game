import pygame as pg

from DataStructures.Stack import Stack

from Controllers.Game.Processes.MainProcess import MainProcess


class GameProcess:
    def __init__(self, game):
        self.game = game

    def do(self, processes_stack: Stack, main_process: MainProcess) -> None:
        self.game.auto_save()
        for event in pg.event.get():
            self.game.states_stack.peek().handle_input(event, processes_stack, main_process)
        self.game.states_stack.peek().update()
        self.game.states_stack.peek().draw()