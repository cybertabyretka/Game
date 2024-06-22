from Controllers.Entities.Physic.BaseEntityPhysic import *
from Controllers.RoomMap.TilePhysic import TileCollision

from Models.Entities.BaseEntity import Entity


class BaseNPCPhysic(BaseEntityPhysic):
    pass


class BaseNPCCollision(BaseEntityCollision):
    def update(self, velocity: list[int], entities: list[Entity], collisions_map: dict[str, TileCollision], movement: tuple[int, int] = (0, 0)) -> dict[str, Entity]:
        get_collisions_around(self.rect, TILE_SIZE, collisions_map, self.collisions_around)
        movement = [movement[0] + velocity[0], movement[1] + velocity[1]]
        if (movement[0] != 0 and movement[1] == 0) or (movement[0] == 0 and movement[1] != 0):
            movement = self.straight_contacts_process(movement)
        elif movement[0] != 0 and movement[1] != 0:
            movement = self.corner_contacts_process(movement)
        movement, entities_around = self.entities_contacts_process(movement, entities)
        self.rect.x += movement[0]
        self.rect.y += movement[1]
        return entities_around
