from Views.Game.Game import GameV

from Utils.Stack import Stack


class Game:
    def __init__(self, surface, rooms_map):
        self.view = GameV(surface, rooms_map)
        self.states_stack = Stack()
        self.entities =