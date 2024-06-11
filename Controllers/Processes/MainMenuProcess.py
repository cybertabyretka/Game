import pygame as pg


class MainMenuProcess:
    def __init__(self, main_menu):
        self.main_menu = main_menu

    def do(self, processes_stack):
        for event in pg.event.get():
            self.main_menu.states_stack.peek().handle_input(event, processes_stack)
        self.main_menu.states_stack.peek().update()
        self.main_menu.states_stack.peek().draw()