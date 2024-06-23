from Controllers.Entities.NPCMind import Mind
from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState
from Controllers.Entities.Physic.NPCsPhysic.BaseNPCPhysic import BaseNPCPhysic

from Models.Entities.BaseEntity import Entity
from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Items.Shield import Shield
from Models.Inventory.Inventory import Inventory


class NPC(Entity):
    def __init__(self, width: int, height: int, start_pos: tuple[int, int], max_velocity: int, current_weapon: Weapon | None, current_shield: Shield | None, max_health: int, current_health: int, inventory: Inventory, paths_asset: dict[str, str], states_types: dict[str, type[NPCBaseState]], physic_type: type[BaseNPCPhysic]):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, physic_type, states_types)
        self.mind: Mind = Mind()
