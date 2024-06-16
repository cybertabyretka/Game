from Views.Entity.Entity import EntityV, PlayerV

from Models.Entity.HealthBar import HealthBar

from Controllers.Entity.EntityPhysic import EntityPhysics, PlayerPhysics, NPCPhysics
from Controllers.Entity.EntityMind import Mind
from Controllers.Entity.States.NPCStates import NPCIdleState
from Controllers.Entity.States.PlayerStates import PlayerIdleState

from Utils.Settings.DataStructures.Stack import Stack


class Entity:
    def __init__(self, width: float, height: float, start_pos, max_velocity, current_weapon, current_shield, max_health, inventory, paths_asset):
        self.view = EntityV(paths_asset)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(PlayerIdleState(self))
        self.current_weapon = current_weapon
        self.current_shield = current_shield
        self.health = HealthBar(max_health)
        self.inventory = inventory


class NPC(Entity):
    def __init__(self, width: float, height: float, start_pos, max_velocity, current_weapon, current_shield, max_health, inventory, paths_asset):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, inventory, paths_asset)
        self.physic = NPCPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(NPCIdleState(self))
        self.mind = Mind()


class Player(Entity):
    def __init__(self, inventory, windows, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=2, current_weapon=None, current_shield=None, max_health=20):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, inventory, paths_asset)
        self.view = PlayerV(windows, paths_asset)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)

    @staticmethod
    def change_current_special_item(special_item, selected_inventory_cell_index, selected_inventory):
        temp = special_item
        special_item = selected_inventory.get_cell(selected_inventory_cell_index).item
        selected_inventory.place_item(selected_inventory_cell_index, temp)
        return special_item


class Swordsman(NPC):
    def __init__(self, inventory, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=1, current_weapon=None, current_shield=None, max_health=2):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, inventory, paths_asset)