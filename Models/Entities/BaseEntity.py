from Models.HealthBar import HealthBar

from Constants.StatesNames import IDLE_STATE

from DataStructures.Stack import Stack

from Views.Entities.Entity import EntityV


class Entity:
    def __init__(self, width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, physic_type, states_types):
        self.view = EntityV(paths_asset)
        self.physic = physic_type(width, height, start_pos, max_velocity)
        self.states_stack = Stack(states_types[IDLE_STATE](self))
        self.current_weapon = current_weapon
        self.current_shield = current_shield
        self.health = HealthBar(max_health, current_health)
        self.inventory = inventory
        self.states_types = states_types
