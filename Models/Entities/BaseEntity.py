from Controllers.Entities.Physic.BaseEntityPhysic import BaseEntityPhysic

from Models.HealthBar import HealthBar

from DataStructures.Stack import Stack

from Views.Entities.Entity import EntityV


class Entity:
    def __init__(self, width, height, start_pos, max_velocity, current_weapon, current_shield, max_health, current_health, inventory, paths_asset, physic_type, idle_state):
        self.view = EntityV(paths_asset)
        self.physic = physic_type(width, height, start_pos, max_velocity)
        self.states_stack = Stack(idle_state)
        self.current_weapon = current_weapon
        self.current_shield = current_shield
        self.health = HealthBar(max_health, current_health)
        self.inventory = inventory
