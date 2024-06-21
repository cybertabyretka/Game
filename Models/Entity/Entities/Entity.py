from Controllers.Entity.Physic.EntityPhysic import EntityPhysics

from Models.Entity.HealthBar import HealthBar

from Utils.Settings.DataStructures.Stack import Stack

from Views.Entity.Entities.Entity import EntityV


class Entity:
    def __init__(self, current_weapon, current_shield, max_health, current_health, inventory, paths_asset):
        self.view = EntityV(paths_asset)
        self.physic: EntityPhysics
        self.states_stack = Stack()
        self.current_weapon = current_weapon
        self.current_shield = current_shield
        self.health = HealthBar(max_health, current_health)
        self.inventory = inventory

    def copy_for_save(self):
        pass
