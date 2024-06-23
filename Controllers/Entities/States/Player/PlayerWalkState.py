import pygame as pg

from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity
from Controllers.CheckMouseButtons import *

from Constants.StatesNames import *

from Models.Room.Room import Room
from Models.Entities.BaseEntity import Entity


class PlayerWalkState(PlayerBaseState):
    def __init__(self, entity: Entity):
        super().__init__(entity)
        self.directions: set[int] = set()

    def handle_input(self, event: pg.event, room: Room) -> None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.directions.add(pg.K_w)
            elif event.key == pg.K_s:
                self.directions.add(pg.K_s)
            elif event.key == pg.K_a:
                self.directions.add(pg.K_a)
            elif event.key == pg.K_d:
                self.directions.add(pg.K_d)
            elif event.key == pg.K_e:
                if not room.live_NPCs_count:
                    mouse_pos = pg.mouse.get_pos()
                    for steal_tile in room.loot_tiles:
                        if steal_tile.collision.rect.collidepoint(mouse_pos):
                            self.entity.states_stack.push(self.entity.states_types[STEAL_STATE](self.entity, steal_tile.inventory))
                            return
                self.entity.states_stack.push(self.entity.states_types[INVENTORY_OPEN_STATE](self.entity))
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.entity.physic.velocity[1] = 0
                if pg.K_w in self.directions:
                    self.directions.remove(pg.K_w)
            elif event.key == pg.K_s:
                self.entity.physic.velocity[1] = 0
                if pg.K_s in self.directions:
                    self.directions.remove(pg.K_s)
            elif event.key == pg.K_a:
                self.entity.physic.velocity[0] = 0
                if pg.K_a in self.directions:
                    self.directions.remove(pg.K_a)
            elif event.key == pg.K_d:
                self.entity.physic.velocity[0] = 0
                if pg.K_d in self.directions:
                    self.directions.remove(pg.K_d)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_left_mouse_button():
                self.entity.states_stack.push(self.entity.states_types[PUNCH_STATE](self.entity))
            elif check_right_mouse_button():
                self.entity.states_stack.push(self.entity.states_types[SHIELD_STATE](self.entity))

    def update(self, room: Room, entities: list[Entity]) -> None:
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
        if len(self.directions) == 0:
            self.entity.states_stack.pop()
            return
        for direction in self.directions:
            if direction == pg.K_w:
                self.entity.view.rotate(0)
                self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
            elif direction == pg.K_s:
                self.entity.view.rotate(180)
                self.entity.physic.velocity[1] = self.entity.physic.max_velocity
            elif direction == pg.K_a:
                self.entity.view.rotate(270)
                self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
            elif direction == pg.K_d:
                self.entity.view.rotate(90)
                self.entity.physic.velocity[0] = self.entity.physic.max_velocity
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map)
