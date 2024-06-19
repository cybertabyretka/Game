from Models.Entity.Entities.Entity import Entity

from Controllers.Entity.Physic.EntityPhysic import EntityPhysics
from Controllers.Entity.NPCMind import Mind


class NPC(Entity):
    def __init__(self, current_weapon, current_shield, max_health, current_health, inventory, paths_asset):
        super().__init__(current_weapon, current_shield, max_health, current_health, inventory, paths_asset)
        self.physic: NPCPhysics
        self.mind = Mind()
