from Controllers.EntityPhysic import EntityPhysics, PlayerPhysics
from Views.Entity import EntityV
import States


class Entity:
    def __init__(self, image, width: float, height: float, start_pos=(350., 350.), max_velocity=1):
        self.entity_view = EntityV(image)
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)
        self.state = States.EntityIdleState(self)


class Player(Entity):
    def __init__(self, image, width=35., height=35., start_pos=(350., 350.), max_velocity=1):
        super().__init__(image, width, height)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)
