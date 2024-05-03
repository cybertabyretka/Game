from Controllers.EntityPhysic import EntityPhysics, PlayerPhysics
from Views.Entity import EntityV


class Entity:
    def __init__(self, image, width: float, height: float, start_pos=(350., 350.), max_velocity=1):
        self.entity_view = EntityV(image)
        self.width: float = width
        self.height: float = height
        self.physic = EntityPhysics(width, height, start_pos, max_velocity)


class Player(Entity):
    def __init__(self, image, width=20., height=20., start_pos=(350., 350.), max_velocity=1):
        super().__init__(image, width, height)
        self.physic = PlayerPhysics(width, height, start_pos, max_velocity)
