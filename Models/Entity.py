from Controllers.EntityPhysic import EntityPhysics
from Views.Entity import EntityV
from Models import States
from Utils.Stack import Stack


class Entity:
    def __init__(self, images_asset, width: float, height: float, start_pos, max_velocity):
        self.entity_view = EntityV(images_asset)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(States.EntityIdleState(self))


class Player(Entity):
    def __init__(self, images_paths, width=35., height=35., start_pos=(350., 350.), max_velocity=1):
        super().__init__(images_paths, width, height, start_pos, max_velocity)
