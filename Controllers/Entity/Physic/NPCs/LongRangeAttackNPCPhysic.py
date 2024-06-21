from Controllers.Entity.Physic.EntityPhysic import EntityPhysics, EntityCollision


class LongRangeAttackNPCCollision(EntityCollision):

    def entities_contacts_process(self, movement, entities):
        entities_around = {'right': None, 'left': None, 'down': None, 'up': None}
        for entity in entities:
            if entity.health.health > 0:
                self.find_entities_intersections(entity, entities_around)
                if movement[0] > 0 and (entity.physic.collision.rect.x - self.rect.topright[0]) >= 0 and abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.height:
                    movement[0] = min(movement[0], entity.physic.collision.rect.x - self.rect.topright[0])
                if movement[0] < 0 and (entity.physic.collision.rect.topright[0] - self.rect.x) <= 0 and abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.height:
                    movement[0] = max(movement[0], entity.physic.collision.rect.topright[0] - self.rect.x)
                if movement[1] > 0 and (entity.physic.collision.rect.y - self.rect.bottomleft[1]) >= 0 and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                    movement[1] = min(movement[1], entity.physic.collision.rect.y - self.rect.bottomleft[1])
                if movement[1] < 0 and (entity.physic.collision.rect.bottomleft[1] - self.rect.y) <= 0 and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
                    movement[1] = max(movement[1], entity.physic.collision.rect.bottomleft[1] - self.rect.y)
        return movement, entities_around

    def find_entities_intersections(self, entity, entities_around):
        if abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.h and (entity.physic.collision.rect.x - self.rect.x) > 0:
            entities_around['right'] = entity
        elif abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.h and (entity.physic.collision.rect.x - self.rect.x) < 0:
            entities_around['left'] = entity
        elif abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.w and (entity.physic.collision.rect.y - self.rect.y) > 0:
            entities_around['down'] = entity
        elif abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.w and (entity.physic.collision.rect.y - self.rect.y) < 0:
            entities_around['up'] = entity

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


class LongRangeAttackNPCPhysic(EntityPhysics):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, LongRangeAttackNPCCollision)