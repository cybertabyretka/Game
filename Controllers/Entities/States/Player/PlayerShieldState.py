import pygame as pg

from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity_with_ready_damage_and_movement, get_damage_and_movement
from Controllers.CheckMouseButtons import *

from Constants.StatesNames import *
from Constants.Colours import *


class PlayerShieldState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.direction = None

    def handle_input(self, event, room):
        if self.finished:
            if event.type == pg.MOUSEBUTTONDOWN and check_right_mouse_button():
                if event.pos[1] < self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 0
                    self.finished = False
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] > self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 90
                    self.finished = False
                elif event.pos[1] > self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 180
                    self.finished = False
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 270
                    self.finished = False
        else:
            if event.type == pg.MOUSEBUTTONUP and not check_right_mouse_button():
                self.finished = True
                self.entity.states_stack.pop()
                self.entity.states_stack.peek().handle_inputs(self.events, room)
            elif event.type == pg.KEYUP or event.type == pg.KEYDOWN:
                self.events.append(event)

    def update(self, room, entities):
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)
        else:
            damage, movement = get_damage_and_movement(room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.physic.collision.rect)
            for damage_type in damage:
                if damage_type in self.entity.current_shield.damage_types:
                    for damage_rect in damage[damage_type]:
                        if damage_rect.direction == 0 and self.direction == 180:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 90 and self.direction == 270:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 180 and self.direction == 0:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 270 and self.direction == 90:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
            check_damage_for_entity_with_ready_damage_and_movement(self.entity, damage, movement, self.entity.states_types[AFTER_PUNCH_STATE])

    def draw(self, surface):
        if self.direction == 0:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y-2, self.entity.physic.collision.rect.width, 2))
        elif self.direction == 90:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x+self.entity.physic.collision.rect.width, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        elif self.direction == 180:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y+self.entity.physic.collision.rect.height, self.entity.physic.collision.rect.width, 2))
        else:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x-2, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))