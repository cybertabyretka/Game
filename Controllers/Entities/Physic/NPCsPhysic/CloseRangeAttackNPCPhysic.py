from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.Entities.Physic.NPCsPhysic.BaseNPCPhysic import *
from Controllers.Entities.Physic.EntitiesProcess import entities_process

from Utils.DistanceCounting import manhattan_distance

from BaseVariables.Others import TILE_SIZE


class CloseRangeAttackNPCCollision(BaseNPCCollision):
    def entities_contacts_process(self, movement, entities):
        entities_around = {'right': None, 'left': None, 'down': None, 'up': None}
        for entity in entities:
            if entity.health.health > 0 and entity.physic.collision is not self and manhattan_distance((entity.physic.collision.collisions_around["center"].rect.x, entity.physic.collision.collisions_around["center"].rect.y), (self.rect.x, self.rect.y)) <= max(self.rect.width, self.rect.height) * 3:
                self.check_distance_between_entities(entity, entities_around)
                entities_process(movement, entity.physic.collision.rect, self.rect)
        return movement, entities_around

    def check_distance_between_entities(self, entity, entities_around):
        if self.rect.topright[0] == entity.physic.collision.rect.x and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
            entities_around['right'] = entity
        if self.rect.x == entity.physic.collision.rect.topright[0] and abs(self.rect.y - entity.physic.collision.rect.y) < entity.physic.collision.rect.height:
            entities_around['left'] = entity
        if self.rect.bottomright[1] == entity.physic.collision.rect.y and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
            entities_around['down'] = entity
        if self.rect.y == entity.physic.collision.rect.bottomright[1] and abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.width:
            entities_around['up'] = entity


class CloseRangeAttackNPCPhysic(BaseNPCPhysic):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, CloseRangeAttackNPCCollision)