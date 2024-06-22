from Controllers.Entities.Physic.BaseEntityPhysic import BaseEntityPhysic, BaseEntityCollision


class PlayerCollision(BaseEntityCollision):
    pass


class PlayerPhysics(BaseEntityPhysic):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, PlayerCollision)
