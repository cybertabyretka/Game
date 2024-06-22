from Controllers.Entities.Physic.NPCsPhysic.BaseNPCPhysic import *
from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.Entities.Physic.EntitiesProcess import entities_process

from BaseVariables.Others import TILE_SIZE


class LongRangeAttackNPCCollision(BaseNPCCollision):
    def entities_contacts_process(self, movement, entities):
        entities_around = {'right': None, 'left': None, 'down': None, 'up': None}
        for entity in entities:
            if entity.health.health > 0:
                self.find_entities_intersections(entity, entities_around)
                entities_process(movement, entity.physic.collision.rect, self.rect)
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


class LongRangeAttackNPCPhysic(BaseNPCPhysic):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, LongRangeAttackNPCCollision)