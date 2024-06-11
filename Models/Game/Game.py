from Views.Game.Game import GameV

from Utils.Stack import Stack


class Game:
    def __init__(self, display, rooms_map, NPCs, player):
        self.view = GameV(display, rooms_map)
        self.states_stack = Stack()
        self.room = rooms_map.get_current_room()
        self.NPCs = NPCs
        self.player = player
        self.entities = [*NPCs, player]