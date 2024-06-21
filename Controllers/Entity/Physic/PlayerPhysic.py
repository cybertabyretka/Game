from Controllers.Entity.Physic.EntityPhysic import EntityPhysics, EntityCollision


class PlayerCollision(EntityCollision):
    pass


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, PlayerCollision)
