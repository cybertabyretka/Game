import time

from BaseVariables.Buttons.Buttons import *
from BaseVariables.Others import TILE_SIZE

from Constants.Date import *

from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.Game.Processes.GameProcess import GameProcess
from Controllers.Game.States.GameStates import Running
from Controllers.Saves.SaveGame import save_game
from Controllers.Saves.SortSaves import saves_indexes_quick_sort

from DataStructures.Stack import Stack

from Views.AppStates.Game import GameV


class Game:
    def __init__(self, display, rooms_map, player, entities_surface, rooms_surface, auto_saves, saves):
        self.view = GameV(display, rooms_map)
        self.states_stack = Stack(Running(self))
        self.room = rooms_map.get_current_room()
        self.player = player
        self.process = GameProcess(self)
        self.entities_surface = entities_surface
        self.rooms_surface = rooms_surface
        self.previous_time_save = time.time()
        self.time_between_saves = 1 * 60
        self.buttons = {'esc_state_buttons': [CONTINUE_BUTTON, SAVE_GAME_BUTTON, EXIT_TO_MAIN_MENU_BUTTON],
                        'save_selection_buttons': [FIRST_SAVE_BUTTON, SECOND_SAVE_BUTTON, THIRD_SAVE_BUTTON, FOURTH_SAVE_BUTTON, FIFTH_SAVE_BUTTON,
                                                   FIRST_AUTO_SAVE_BUTTON, SECOND_AUTO_SAVE_BUTTON, THIRD_AUTO_SAVE_BUTTON, FOURTH_AUTO_SAVE_BUTTON, FIFTH_AUTO_SAVE_BUTTON,
                                                   CANSEL_BUTTON]}
        self.auto_saves = auto_saves
        self.auto_saves_indexes = [i for i in range(len(auto_saves))]
        self.current_auto_save_index = 0
        self.sort_auto_saves_indexes()
        self.saves = saves

    def auto_save(self):
        current_time = time.time()
        if current_time - self.previous_time_save >= self.time_between_saves:
            self.previous_time_save = current_time
            save_game(self.auto_saves[self.auto_saves_indexes[self.current_auto_save_index]], self.view.rooms_map.copy_for_save(self.room), self.player.copy_for_save())
            self.current_auto_save_index = (self.current_auto_save_index + 1) % len(self.auto_saves)

    def sort_auto_saves_indexes(self):
        indexes_with_no_data = []
        indexes_with_data = []
        saves_with_date = []
        for i in range(len(self.auto_saves)):
            current_date, current_time = self.auto_saves[i].get_date().split()
            if current_date == BASE_DATE or current_time == BASE_TIME:
                indexes_with_no_data.append(i)
            else:
                saves_with_date.append(self.auto_saves[i])
                indexes_with_data.append(i)
        saves_indexes_quick_sort(saves_with_date, indexes_with_data)
        self.auto_saves_indexes = [*indexes_with_no_data, *indexes_with_data]

    def new_object_preprocess(self, doors_connections):
        self.view.rooms_map.new_object_preprocess(doors_connections)
        self.download_entities()

    def after_load_preprocess(self):
        self.view.rooms_map.after_load_preprocess()
        self.download_entities()

    def copy_for_save(self):
        return self.player.copy_for_save(), self.view.rooms_map.copy_for_save()

    def download_entities(self):
        for i in range(self.view.rooms_map.size[0]):
            for j in range(self.view.rooms_map.size[1]):
                if self.view.rooms_map.map[i][j] is not None:
                    self.view.rooms_map.map[i][j].download_map()
                    for NPC in self.view.rooms_map.map[i][j].NPCs:
                        NPC.view.download_images(NPC.current_weapon, NPC.current_shield, NPC.inventory)
                        get_collisions_around(NPC.physic.collision.rect, TILE_SIZE, self.room.collisions_map.map, NPC.physic.collision.collisions_around)
        self.player.view.download_images(self.player.current_weapon, self.player.current_shield, self.player.inventory)