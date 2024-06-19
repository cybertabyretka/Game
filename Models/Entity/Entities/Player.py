from Models.Entity.Entities.Entity import Entity

from Controllers.Entity.Physic.PlayerPhysic import PlayerPhysics
from Controllers.Entity.States.PlayerStates import PlayerIdleState

from Utils.Settings.DataStructures.Stack import Stack

from Views.Entity.Entities.Player import PlayerV


class Player(Entity):
    def __init__(self, inventory, windows, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=2, current_weapon=None, current_shield=None, max_health=20, current_health=20):
        super().__init__(current_weapon, current_shield, max_health, current_health, inventory, paths_asset)
        self.view = PlayerV(windows, paths_asset)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(PlayerIdleState(self))

    @staticmethod
    def change_current_special_item(special_item, selected_cell):
        special_item, selected_cell.item = selected_cell.item, special_item
        return special_item

    def copy_for_save(self):
        return Player(self.inventory.copy_for_save(), self.view.windows, self.view.paths_asset,
                      width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                      max_velocity=self.physic.max_velocity,
                      current_weapon=self.current_weapon.copy_for_save(), current_shield=self.current_shield.copy_for_save(),
                      max_health=self.health.max_health, current_health=self.health.health)