import pygame as pg

from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity
from Controllers.CheckMouseButtons import *

from Constants.StatesNames import *

from Utils.DistanceCounting import manhattan_distance

from Models.Room.Room import Room
from Models.Entities.BaseEntity import Entity


class PlayerIdleState(PlayerBaseState):
    def handle_input(self, event: pg.event, room: Room) -> None:
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                self.entity.states_stack.push(self.entity.states_types[WALK_STATE](self.entity))
            elif event.key == pg.K_e:
                if not room.live_NPCs_count:
                    mouse_pos = pg.mouse.get_pos()
                    for steal_tile in room.loot_tiles:
                        if steal_tile.collision.rect.collidepoint(mouse_pos) and manhattan_distance(steal_tile.collision.rect.topleft, self.entity.physic.collision.rect.topleft) <= min(self.entity.physic.collision.rect.w, self.entity.physic.collision.rect.h) * 2:
                            self.entity.states_stack.push(self.entity.states_types[STEAL_STATE](self.entity, steal_tile.inventory))
                            return
                    self.entity.states_stack.push(self.entity.states_types[INVENTORY_OPEN_STATE](self.entity))
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_left_mouse_button():
                self.entity.states_stack.push(self.entity.states_types[PUNCH_STATE](self.entity))
            elif check_right_mouse_button():
                self.entity.states_stack.push(self.entity.states_types[SHIELD_STATE](self.entity))

    def update(self, room: Room, entities: list[Entity]) -> None:
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
