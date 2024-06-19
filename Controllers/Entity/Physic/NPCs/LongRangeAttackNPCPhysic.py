from Controllers.Entity.Physic.EntityPhysic import EntityPhysics, EntityCollision


class LongRangeAttackNPCCollision(EntityCollision):
    def __init__(self, pos, size):
        super().__init__(pos, size)


class LongRangeAttackNPCPhysic(EntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(max_velocity)
        self.collision = LongRangeAttackNPCCollision(start_pos, (width, height))