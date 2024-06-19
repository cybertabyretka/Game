from Controllers.Entity.Physic.EntityPhysic import EntityPhysics, EntityCollision


class PlayerCollision(EntityCollision):
    def __init__(self, pos, size):
        super().__init__(pos, size)


class PlayerPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity)
        self.collision = PlayerCollision(start_pos, (width, height))