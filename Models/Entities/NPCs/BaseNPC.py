from Controllers.Entities.NPCMind import Mind

from Models.Entities.BaseEntity import Entity


class NPC(Entity):
    def __init__(self, width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, states_types, physic_type, idle_state):
        super().__init__(width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, physic_type, idle_state)
        self.states_types = states_types
        self.mind = Mind()