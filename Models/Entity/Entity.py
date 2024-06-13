from Views.Entity.Entity import EntityV, PlayerV

from Models.Entity.HealthBar import HealthBar

from Controllers.Entity.EntityPhysic import EntityPhysics, PlayerPhysics, NPCPhysics
from Controllers.Entity.EntityMind import Mind
from Controllers.Entity.States.NPCStates import NPCIdleState
from Controllers.Entity.States.PlayerStates import PlayerIdleState

from Utils.Stack import Stack


class Entity:
    def __init__(self, images_asset, width: float, height: float, start_pos, max_velocity, current_weapon, surface, max_health):
        self.view = EntityV(images_asset, surface)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(PlayerIdleState(self))
        self.current_weapon = current_weapon
        self.health = HealthBar(max_health)


class NPC(Entity):
    def __init__(self, images_paths, width: float, height: float, start_pos, max_velocity, current_weapon, surface, max_health):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_weapon, surface, max_health)
        self.physic = NPCPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(NPCIdleState(self))
        self.mind = Mind()


class Player(Entity):
    def __init__(self, images_paths, surface, inventory, windows, width=35., height=35., start_pos=(0, 0), max_velocity=2, current_weapon=None, current_shield=None, max_health=20):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_weapon, surface, max_health)
        self.view = PlayerV(images_paths, surface, windows)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)
        self.inventory = inventory
        self.current_shield = current_shield


class Swordsman(NPC):
    def __init__(self, images_paths, surface, width=35., height=35., start_pos=(0, 0), max_velocity=1, current_weapon=None, max_health=2):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_weapon, surface, max_health)