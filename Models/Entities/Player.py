from Controllers.Entities.Physic.PlayerPhysic import PlayerPhysics

from BaseVariables.Entities.PlayerStatesTypes import PLAYER_STATES_TYPES

from Models.Entities.BaseEntity import Entity
from Models.Inventory.Inventory import Inventory
from Models.InteractionObjects.InGameWindow import InGameWindow
from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Items.Shield import Shield
from Models.Inventory.InventoryCell import InventoryCell
from Models.Items.Item import Item

from DataStructures.Stack import Stack

from Views.Entities.Player import PlayerV


class Player(Entity):
    def __init__(self, inventory: Inventory, windows: dict[str, InGameWindow], paths_asset: dict[str, str], width: int = 35., height: int = 35., start_pos: tuple[int, int] = (0, 0), max_velocity: int = 2, current_weapon: Weapon | None = None, current_shield: Shield | None = None, max_health: int = 20, current_health: int = 20):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, PlayerPhysics, PLAYER_STATES_TYPES)
        self.view: PlayerV = PlayerV(windows, paths_asset)

    @staticmethod
    def change_current_special_item(special_item: Weapon | Shield, selected_cell: InventoryCell) -> Weapon | Shield | Item:
        special_item, selected_cell.item = selected_cell.item, special_item
        return special_item

    def copy_for_save(self):
        return Player(self.inventory.copy_for_save(), self.view.windows, self.view.paths_asset,
                      width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                      max_velocity=self.physic.max_velocity,
                      current_weapon=self.current_weapon.copy_for_save(), current_shield=self.current_shield.copy_for_save(),
                      max_health=self.health.max_health, current_health=self.health.health)