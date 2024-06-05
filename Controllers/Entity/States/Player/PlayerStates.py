import pygame as pg

from Controllers.Entity.States.Utils import get_damage_and_direction
from Controllers.Entity.States.BaseStates import State


def check_damage_for_player(entity, damage_map):
    damage, movement = get_damage_and_direction(damage_map, entity.physic.collision.rect)
    if damage:
        entity.states_stack.push(PlayerAfterPunchState(entity))
        entity.states_stack.peek().movement = movement
        entity.states_stack.peek().damage = damage
        return True
    return False


class PlayerAfterPunchState(State):
    def __init__(self, entity):
        super().__init__(entity)
        self.movement = (0, 0)
        self.damage = 0
        self.events = []

    def handle_input(self, event, room):
        if len(self.events) < 20:
            self.events.append(event)

    def update(self, room, entities):
        self.entity.health.health -= self.damage
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()
        self.entity.states_stack.peek().handle_inputs(self.events, room)


class PlayerIdleState(State):
    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                self.entity.states_stack.push(PlayerWalkState(self.entity))
        if event.type == pg.MOUSEBUTTONDOWN:
            self.entity.states_stack.push(PlayerPunchState(self.entity))

    def update(self, room, entities):
        check_damage_for_player(self.entity, room.collisions_map.damage_map)


class PlayerWalkState(State):
    def __init__(self, entity):
        super().__init__(entity)
        self.directions = set()

    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.directions.add(pg.K_w)
            if event.key == pg.K_s:
                self.directions.add(pg.K_s)
            if event.key == pg.K_a:
                self.directions.add(pg.K_a)
            if event.key == pg.K_d:
                self.directions.add(pg.K_d)
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.entity.physic.velocity[1] = 0
                if pg.K_w in self.directions:
                    self.directions.remove(pg.K_w)
            if event.key == pg.K_s:
                self.entity.physic.velocity[1] = 0
                if pg.K_s in self.directions:
                    self.directions.remove(pg.K_s)
            if event.key == pg.K_a:
                self.entity.physic.velocity[0] = 0
                if pg.K_a in self.directions:
                    self.directions.remove(pg.K_a)
            if event.key == pg.K_d:
                self.entity.physic.velocity[0] = 0
                if pg.K_d in self.directions:
                    self.directions.remove(pg.K_d)
        elif event.type == pg.MOUSEBUTTONDOWN:
            self.entity.states_stack.push(PlayerPunchState(self.entity))

    def update(self, room, entities):
        if check_damage_for_player(self.entity, room.collisions_map.damage_map):
            return
        if len(self.directions) == 0:
            self.entity.states_stack.pop()
            return
        for direction in self.directions:
            if direction == pg.K_w:
                self.entity.entity_view.rotate(0)
                self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
            elif direction == pg.K_s:
                self.entity.entity_view.rotate(180)
                self.entity.physic.velocity[1] = self.entity.physic.max_velocity
            elif direction == pg.K_a:
                self.entity.entity_view.rotate(270)
                self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
            elif direction == pg.K_d:
                self.entity.entity_view.rotate(90)
                self.entity.physic.velocity[0] = self.entity.physic.max_velocity
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities)


class PlayerPunchState(State):
    def __init__(self, entity):
        super().__init__(entity)
        self.events = []

    def handle_input(self, event, room):
        if check_damage_for_player(self.entity, room.collisions_map.damage_map):
            return
        if self.finished:
            self.events = []
            if pg.mouse.get_pressed(3)[0] and event.type == pg.MOUSEBUTTONDOWN:
                if event.pos[1] < self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.entity.current_item.set_animation(0, self.entity)
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] > self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.entity.current_item.set_animation(90, self.entity)
                elif event.pos[1] > self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.entity.current_item.set_animation(180, self.entity)
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.entity.current_item.set_animation(270, self.entity)
                if self.entity.current_item.weapon_view.copied_animation is not None:
                    room.collisions_map.add_damage(self.entity.current_item.physic.attack_physic, id(self.entity.current_item.physic.attack_physic))
                    self.finished = False
                else:
                    self.finished = True
                    self.entity.states_stack.pop()
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif (event.type == pg.KEYUP or event.type == pg.KEYDOWN) and len(self.events) < 20:
            self.events.append(event)

    def update(self, room, entities):
        if self.entity.current_item.weapon_view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, screen):
        self.entity.entity_view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        self.entity.current_item.weapon_view.copied_animation.render(screen)