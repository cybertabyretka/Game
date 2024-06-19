from Controllers.Entity.Physic.EntityPhysic import EntityPhysics, EntityCollision

from Utils.DistanceCounting import manhattan_distance


class CloseRangeAttackNPCCollision(EntityCollision):
    def __init__(self, pos, size):
        super().__init__(pos, size)

    def entities_contacts_process(self, movement, entities):
        entities_around = {'right': None, 'left': None, 'down': None, 'up': None}
        for entity in entities:
            if entity.physic.collision is not self and manhattan_distance((entity.physic.collision.collisions_around["center"].rect.x, entity.physic.collision.collisions_around["center"].rect.y), (self.rect.x, self.rect.y)) <= max(self.rect.width, self.rect.height) * 3:
                entities_around = self.check_distance_between_entities(entity, entities_around)
                if movement[0] > 0 and (entity.physic.collision.rect.x - self.rect.topright[0]) >= 0 and abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.height:
                    movement[0] = min(movement[0], entity.physic.collision.rect.x - self.rect.topright[0])
                if movement[0] < 0 and (entity.physic.collision.rect.topright[0] - self.rect.x) <= 0 and abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.height:
                    movement[0] = max(movement[0], entity.physic.collision.rect.topright[0] - self.rect.x)
                if movement[1] > 0 and (entity.physic.collision.rect.y - self.rect.bottomleft[1]) >= 0 and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                    movement[1] = min(movement[1], entity.physic.collision.rect.y - self.rect.bottomleft[1])
                if movement[1] < 0 and (entity.physic.collision.rect.bottomleft[1] - self.rect.y) <= 0 and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                    movement[1] = max(movement[1], entity.physic.collision.rect.bottomleft[1] - self.rect.y)
        return movement, entities_around

    def update(self, velocity, entities, movement=(0, 0)):
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        if (movement[0] != 0 and movement[1] == 0) or (movement[0] == 0 and movement[1] != 0):
            movement = self.straight_contacts_process(movement)
        elif movement[0] != 0 and movement[1] != 0:
            movement = self.corner_contacts_process(movement)
        movement, entities_around = self.entities_contacts_process(movement, entities)
        self.rect.x += movement[0]
        self.rect.y += movement[1]
        return entities_around

    def check_distance_between_entities(self, entity, entities_around):
        if self.rect.topright[0] == entity.physic.collision.rect.x and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
            entities_around['right'] = entity
        if self.rect.x == entity.physic.collision.rect.topright[0] and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
            entities_around['left'] = entity
        if self.rect.bottomright[1] == entity.physic.collision.rect.y and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
            entities_around['down'] = entity
        if self.rect.y == entity.physic.collision.rect.bottomright[1] and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
            entities_around['up'] = entity
        return entities_around


class CloseRangeAttackNPCPhysics(EntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(max_velocity)
        self.collision = CloseRangeAttackNPCCollision(start_pos, (width, height))