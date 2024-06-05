from Controllers.Entity.EntityPhysic import EntityPhysics
from Controllers.Entity.EntityMind import Mind
from Views.Entity import EntityV
from Controllers.Entity import EntityStates
from Utils.Stack import Stack


class Entity:
    def __init__(self, images_asset, width: float, height: float, start_pos, max_velocity, current_item, surface, max_health):
        self.entity_view = EntityV(images_asset, surface)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(EntityStates.PlayerIdleState(self))
        self.current_item = current_item
        self.health = max_health


class NPC(Entity):
    def __init__(self, images_paths, width: float, height: float, start_pos, max_velocity, current_item, surface, max_health):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_item, surface, max_health)
        self.states_stack = Stack(EntityStates.NPCIdleState(self))
        self.mind = Mind()


class Player(Entity):
    def __init__(self, images_paths, surface, width=35., height=35., start_pos=(350., 350.), max_velocity=2, current_item=None, max_health=20):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_item, surface, max_health)


class Swordsman(NPC):
    def __init__(self, images_paths, surface, width=35., height=35., start_pos=(120., 120.), max_velocity=1, current_item=None, max_health=20):
        super().__init__(images_paths, width, height, start_pos, max_velocity, current_item, surface, max_health)