from Views.Game.Game import GameV

from Utils.Settings.DataStructures.Stack import Stack
from Utils.Settings.Buttons.Buttons import *

from Controllers.Processes.GameProcess import GameProcess
from Controllers.Game.GameStates import Running


class Game:
    def __init__(self, display, rooms_map, player, entities_surface, rooms_surface):
        self.view = GameV(display, rooms_map)
        self.states_stack = Stack(Running(self))
        self.room = rooms_map.get_current_room()
        self.player = player
        self.process = GameProcess(self)
        self.entities_surface = entities_surface
        self.rooms_surface = rooms_surface
        self.buttons = {'esc_state_buttons': [CONTINUE_BUTTON, SAVE_GAME_BUTTON, EXIT_TO_MAIN_MENU_BUTTON]}

    def download_images(self):
        self.view.rooms_map.download_images()
        self.player.view.download_images(self.player.current_weapon, self.player.current_shield, self.player.inventory)

    def copy_for_save(self):
        return self.player.copy_for_save(), self.view.rooms_map.copy_for_save()