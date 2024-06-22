from Controllers.Entities.Physic.BaseEntityPhysic import BaseEntityPhysic, BaseEntityCollision


class PlayerCollision(BaseEntityCollision):
    pass


class PlayerPhysics(BaseEntityPhysic):
    def __init__(self, width: int, height: int, start_pos: tuple[int, int], max_velocity: int):
        super().__init__(width, height, start_pos, max_velocity, PlayerCollision)
