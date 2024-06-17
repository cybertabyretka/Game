from Views.Entity.Entity import EntityV, PlayerV

from Models.Entity.HealthBar import HealthBar

from Controllers.Entity.EntityPhysic import EntityPhysics, PlayerPhysics, NPCPhysics
from Controllers.Entity.EntityMind import Mind
from Controllers.Entity.States.NPCStates import NPCIdleState
from Controllers.Entity.States.PlayerStates import PlayerIdleState

from Utils.Settings.DataStructures.Stack import Stack


class Entity:
    def __init__(self, width: float, height: float, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset):
        self.view = EntityV(paths_asset)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(PlayerIdleState(self))
        self.current_weapon = current_weapon
        self.current_shield = current_shield
        self.health = HealthBar(max_health, current_health)
        self.inventory = inventory

    def copy_for_save(self):
        return Entity(self.physic.collision.rect.w, self.physic.collision.rect.h, self.physic.collision.rect.topleft, self.physic.max_velocity, self.current_weapon.copy_for_save(), self.current_shield.copy_for_save(), self.health.max_health, self.health.health, self.inventory.copy_for_save(), self.view.paths_asset)


class NPC(Entity):
    def __init__(self, width: float, height: float, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset)
        self.physic = NPCPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(NPCIdleState(self))
        self.mind = Mind()

    def copy_for_save(self):
        return NPC(self.physic.collision.rect.w, self.physic.collision.rect.h, self.physic.collision.rect.topleft, self.physic.max_velocity, self.current_weapon.copy_for_save(), self.current_shield.copy_for_save(), self.health.max_health, self.health.health, self.inventory.copy_for_save(), self.view.paths_asset)


class Player(Entity):
    def __init__(self, inventory, windows, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=2, current_weapon=None, current_shield=None, max_health=20, current_health=20):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset)
        self.view = PlayerV(windows, paths_asset)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)

    @staticmethod
    def change_current_special_item(special_item, selected_inventory_cell_index, selected_inventory):
        temp = special_item
        special_item = selected_inventory.get_cell(selected_inventory_cell_index).item
        selected_inventory.place_item(selected_inventory_cell_index, temp)
        return special_item

    def copy_for_save(self):
        return Player(self.inventory.copy_for_save(), self.view.windows, self.view.paths_asset,
                      width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                      max_velocity=self.physic.max_velocity,
                      current_weapon=self.current_weapon.copy_for_save(), current_shield=self.current_shield.copy_for_save(),
                      max_health=self.health.max_health, current_health=self.health.health)


class Swordsman(NPC):
    def __init__(self, inventory, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=1, current_weapon=None, current_shield=None, max_health=2, current_health=2):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset)

    def copy_for_save(self):
        return Swordsman(self.inventory.copy_for_save(), self.view.paths_asset,
                         width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                         max_velocity=self.physic.max_velocity,
                         current_weapon=self.current_weapon.copy_for_save(), current_shield=self.current_shield.copy_for_save(),
                         max_health=self.health.max_health, current_health=self.health.health)