import time

from Controllers.Entities.Physic.NPCsPhysic.LongRangeAttackNPCPhysic import LongRangeAttackNPCPhysic

from BaseVariables.Entities.WizardStatesTypes import *

from Models.Entities.NPCs.BaseNPC import NPC
from Models.Inventory.Inventory import Inventory
from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Items.Shield import Shield


class Wizard(NPC):
    def __init__(self, inventory: Inventory, paths_asset: dict[str, str], width: int = 35., height: int = 35., start_pos: tuple[int, int] = (0, 0), max_velocity: int = 1, current_weapon: Weapon | None = None, current_shield: Weapon | None = None, max_health: int = 10, current_health: int = 10):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, WIZARD_STATES_TYPES, LongRangeAttackNPCPhysic)
        self.time_since_previous_attack: float = time.time()
        self.break_time: int = 3

    def copy_for_save(self):
        return Wizard(self.inventory.copy_for_save(), self.view.paths_asset,
                      width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                      max_velocity=self.physic.max_velocity,
                      current_weapon=self.current_weapon.copy_for_save(),
                      max_health=self.health.max_health, current_health=self.health.health)