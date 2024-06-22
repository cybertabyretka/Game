from Controllers.Entities.Physic.NPCsPhysic.BaseNPCPhysic import *
from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around
from Controllers.Entities.Physic.EntitiesProcess import entities_process

from Constants.Directions import *

from BaseVariables.Others import TILE_SIZE


class LongRangeAttackNPCCollision(BaseNPCCollision):
    def entities_contacts_process(self, movement: list[int], entities: list[Entity]) -> tuple[list[int], dict[str, Entity | None]]:
        entities_around: dict[str, Entity | None] = {RIGHT: None, LEFT: None, DOWN: None, UP: None}
        for entity in entities:
            if entity.health.health > 0:
                self.find_entities_intersections(entity, entities_around)
                entities_process(movement, entity.physic.collision.rect, self.rect)
        return movement, entities_around

    def find_entities_intersections(self, entity, entities_around):
        if abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.h and (entity.physic.collision.rect.x - self.rect.x) > 0:
            entities_around[RIGHT] = entity
        elif abs(self.rect.y - entity.physic.collision.rect.y) < self.rect.h and (entity.physic.collision.rect.x - self.rect.x) < 0:
            entities_around[LEFT] = entity
        elif abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.w and (entity.physic.collision.rect.y - self.rect.y) > 0:
            entities_around[DOWN] = entity
        elif abs(self.rect.x - entity.physic.collision.rect.x) < self.rect.w and (entity.physic.collision.rect.y - self.rect.y) < 0:
            entities_around[UP] = entity


class LongRangeAttackNPCPhysic(BaseNPCPhysic):
    def __init__(self, width, height, start_pos, max_velocity):
        super().__init__(width, height, start_pos, max_velocity, LongRangeAttackNPCCollision)