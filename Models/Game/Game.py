from Views.Game.Game import GameV

from Utils.Stack import Stack

from Controllers.Processes.GameProcess import GameProcess
from Controllers.Game.Game.GameStates import GameOn


class Game:
    def __init__(self, display, rooms_map, player):
        self.view = GameV(display, rooms_map)
        self.states_stack = Stack(GameOn(self))
        self.room = rooms_map.get_current_room()
        self.player = player
        self.process = GameProcess(self)