from Controllers.Entities.Physic.BaseEntityPhysic import BaseEntityPhysics, BaseEntityCollision


class PlayerCollision(BaseEntityCollision):
    pass


class PlayerPhysics(BaseEntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, PlayerCollision)
