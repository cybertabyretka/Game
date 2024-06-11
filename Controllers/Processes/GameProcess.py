import pygame as pg


class GameProcess:
    def __init__(self, game):
        self.game = game

    def do(self, processes_stack):
        for event in pg.event.get():
            self.game.states_stack.peek().handle_input(event, processes_stack)
        self.game.states_stack.peek().update()
        self.game.states_stack.peek().draw()