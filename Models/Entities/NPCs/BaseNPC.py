from Controllers.Entities.NPCMind import Mind

from Models.Entities.BaseEntity import Entity


class NPC(Entity):
    def __init__(self, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, states_types):
        super().__init__(current_weapon, current_shield, max_health, current_health, inventory, paths_asset)
        self.states_types = states_types
        self.physic: NPCPhysics
        self.mind = Mind()
