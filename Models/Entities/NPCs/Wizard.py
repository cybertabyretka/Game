import time

from Controllers.Entities.Physic.NPCsPhysic.LongRangeAttackNPCPhysic import LongRangeAttackNPCPhysic
from Controllers.Entities.States.NPCs.WizardStates import WizardIdleState

from BaseVariables.Entities.WizardStatesTypes import *

from Models.Entities.NPCs.BaseNPC import NPC


class Wizard(NPC):
    def __init__(self, inventory, paths_asset, width=35., height=35., start_pos=(0, 0), max_velocity=1, current_weapon=None, current_shield=None, max_health=2, current_health=2):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, WIZARD_STATES_TYPES, LongRangeAttackNPCPhysic, WizardIdleState(self))
        self.time_since_previous_attack = time.time()
        self.break_time = 5

    def copy_for_save(self):
        return Wizard(self.inventory.copy_for_save(), self.view.paths_asset,
                      width=self.physic.collision.rect.w, height=self.physic.collision.rect.h, start_pos=self.physic.collision.rect.topleft,
                      max_velocity=self.physic.max_velocity,
                      current_weapon=self.current_weapon.copy_for_save(),
                      max_health=self.health.max_health, current_health=self.health.health)