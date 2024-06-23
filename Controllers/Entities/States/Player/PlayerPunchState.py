from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity
from Controllers.CheckMouseButtons import *

from Constants.StatesNames import *


class PlayerPunchState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.copied_damage_physic = None

    def handle_input(self, event, room):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
        if self.finished:
            self.events = []
            if event.type == pg.MOUSEBUTTONDOWN and check_left_mouse_button():
                direction = -1
                if event.pos[1] < self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 0
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] > self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 90
                elif event.pos[1] > self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 180
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 270
                if self.entity.current_weapon.attack(room, direction, self.entity, self):
                    self.finished = False
                else:
                    self.finished = True
                    self.entity.states_stack.pop()
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif (event.type == pg.KEYUP or event.type == pg.KEYDOWN) and len(self.events) < 35:
            self.events.append(event)

    def update(self, room, entities):
        if self.entity.current_weapon.view.copied_animation is not None:
            if self.entity.current_weapon.view.copied_animation.done:
                self.finished = True
                room.collisions_map.remove_damage(id(self.copied_damage_physic))
                self.entity.states_stack.pop()
                self.entity.states_stack.peek().handle_inputs(self.events, room)
        else:
            self.finished = True
            room.collisions_map.remove_damage(id(self.copied_damage_physic))
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, surface):
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_weapon.view.copied_animation.draw(surface)