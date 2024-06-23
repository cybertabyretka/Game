from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState
from Controllers.Weapons.AttackPhysic import AttackPhysic
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity

from Constants.StatesNames import *
from Constants.Directions import *

from Models.Entities.BaseEntity import Entity


class NPCPunchState(NPCBaseState):
    def __init__(self, entity: Entity, direction_for_punch: str):
        super().__init__(entity)
        self.direction_for_punch: str = direction_for_punch
        self.copied_damage_physic: AttackPhysic | None = None

    def update(self, room, player, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
        if self.finished:
            if self.direction_for_punch == UP:
                direction = 0
            elif self.direction_for_punch == RIGHT:
                direction = 90
            elif self.direction_for_punch == DOWN:
                direction = 180
            else:
                direction = 270
            if self.entity.current_weapon.attack(room, direction, self.entity, self):
                self.finished = False
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif self.entity.current_weapon.view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.copied_damage_physic))
            self.entity.states_stack.pop()

    def draw(self, surface):
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_weapon.view.copied_animation.draw(surface)