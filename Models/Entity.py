from Controllers.EntityPhysic import EntityPhysics
from Views.Entity import EntityV
from Models import States
from Utils.Stack import Stack
from Utils.Picture import Picture


class Entity:
    def __init__(self, image_path: str, width: float, height: float, start_pos, max_velocity):
        self.entity_view = EntityV(image_path)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.states_stack = Stack(States.EntityIdleState(self))


class Player(Entity):
    def __init__(self, image, width=35., height=35., start_pos=(350., 350.), max_velocity=1):
        super().__init__(image, width, height, start_pos, max_velocity)
