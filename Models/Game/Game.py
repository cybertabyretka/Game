from Views.Game.Game import GameV

from Utils.Settings.DataStructures.Stack import Stack
from Utils.Settings.Buttons.Buttons import *
from Utils.Setting import TILE_SIZE

from Controllers.Processes.GameProcess import GameProcess
from Controllers.Game.GameStates import Running


class Game:
    def __init__(self, display, rooms_map, player, entities_surface, rooms_surface, auto_saves, saves):
        self.view = GameV(display, rooms_map)
        self.states_stack = Stack(Running(self))
        self.room = rooms_map.get_current_room()
        self.player = player
        self.process = GameProcess(self)
        self.entities_surface = entities_surface
        self.rooms_surface = rooms_surface
        self.buttons = {'esc_state_buttons': [CONTINUE_BUTTON, SAVE_GAME_BUTTON, EXIT_TO_MAIN_MENU_BUTTON],
                        'save_selection_buttons': [FIRST_SAVE_BUTTON, SECOND_SAVE_BUTTON, THIRD_SAVE_BUTTON, FOURTH_SAVE_BUTTON, FIFTH_SAVE_BUTTON,
                                                   FIRST_AUTO_SAVE_BUTTON, SECOND_AUTO_SAVE_BUTTON, THIRD_AUTO_SAVE_BUTTON, FOURTH_AUTO_SAVE_BUTTON, FIFTH_AUTO_SAVE_BUTTON]}
        self.auto_saves = auto_saves
        self.saves = saves

    def download_images(self):
        self.view.rooms_map.download_images()
        self.player.view.download_images(self.player.current_weapon, self.player.current_shield, self.player.inventory)

    def copy_for_save(self):
        return self.player.copy_for_save(), self.view.rooms_map.copy_for_save()

    def download_entities(self):
        for i in range(self.view.rooms_map.size[1]):
            for j in range(self.view.rooms_map.size[0]):
                if self.view.rooms_map.map[i][j] is not None:
                    self.view.rooms_map.map[i][j].download_map()
                    for NPC in self.view.rooms_map.map[i][j].NPCs:
                        NPC.physic.collision.get_collisions_around(self.view.rooms_map.map[i][j].collisions_map.map, TILE_SIZE)
        self.player.physic.collision.get_collisions_around(self.room.collisions_map.map, TILE_SIZE)