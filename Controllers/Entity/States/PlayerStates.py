import pygame as pg

from Utils.Setting import GRAY_RGB

from Controllers.Entity.States.Utils import get_damage_and_movement
from Controllers.Entity.States.BaseStates import PlayerState


def check_damage_for_player(entity, damage_map):
    damage, movement = get_damage_and_movement(damage_map, entity.physic.collision.rect)
    if damage:
        entity.states_stack.push(PlayerAfterPunchState(entity))
        entity.states_stack.peek().movement = movement
        entity.states_stack.peek().damage = damage
        return True
    return False


def check_damage_for_player_with_ready_damage_and_movement(entity, damage, movement):
    if damage:
        entity.states_stack.push(PlayerAfterPunchState(entity))
        entity.states_stack.peek().movement = movement
        entity.states_stack.peek().damage = damage
        return True
    return False


class PlayerShieldState(PlayerState):
    def __init__(self, entity):
        super().__init__(entity)
        self.direction = None
        self.events = []

    def handle_input(self, event, room):
        if self.finished:
            if event.type == pg.MOUSEBUTTONDOWN and pg.mouse.get_pressed(3)[2]:
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
            if event.type == pg.MOUSEBUTTONUP and not pg.mouse.get_pressed(3)[2]:
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
            damage, movement = get_damage_and_movement(room.collisions_map.damage_map, self.entity.physic.collision.rect)
            for damage_type in damage:
                if damage_type == 'sword':
                    for damage_rect in damage[damage_type]:
                        if damage_rect.direction == 0 and self.direction == 180:
                            damage_rect.damage = 0
                        elif damage_rect.direction == 90 and self.direction == 270:
                            damage_rect.damage = 0
                        elif damage_rect.direction == 180 and self.direction == 0:
                            damage_rect.damage = 0
                        elif damage_rect.direction == 270 and self.direction == 90:
                            damage_rect.damage = 0
            check_damage_for_player_with_ready_damage_and_movement(self.entity, damage, movement)

    def draw(self):
        if self.direction == 0:
            pg.draw.rect(self.entity.view.surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y-2, self.entity.physic.collision.rect.width, 2))
        elif self.direction == 90:
            pg.draw.rect(self.entity.view.surface, GRAY_RGB, (self.entity.physic.collision.rect.x+self.entity.physic.collision.rect.width, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        elif self.direction == 180:
            pg.draw.rect(self.entity.view.surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y+self.entity.physic.collision.rect.height, self.entity.physic.collision.rect.width, 2))
        else:
            pg.draw.rect(self.entity.view.surface, GRAY_RGB, (self.entity.physic.collision.rect.x-2, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        self.entity.view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class PlayerAfterPunchState(PlayerState):
    def __init__(self, entity):
        super().__init__(entity)
        self.movement = (0, 0)
        self.damage = {}
        self.events = []

    def handle_input(self, event, room):
        if len(self.events) < 35:
            self.events.append(event)

    def update(self, room, entities):
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage
        self.entity.health.health -= damage
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()
        self.entity.states_stack.peek().handle_inputs(self.events, room)


class PlayerIdleState(PlayerState):
    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                self.entity.states_stack.push(PlayerWalkState(self.entity))
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed(3)[0]:
                self.entity.states_stack.push(PlayerPunchState(self.entity))
            elif pg.mouse.get_pressed(3)[2]:
                self.entity.states_stack.push(PlayerShieldState(self.entity))

    def update(self, room, entities):
        if check_damage_for_player(self.entity, room.collisions_map.damage_map):
            return


class PlayerWalkState(PlayerState):
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
            if pg.mouse.get_pressed(3)[0]:
                self.entity.states_stack.push(PlayerPunchState(self.entity))
            elif pg.mouse.get_pressed(3)[2]:
                self.entity.states_stack.push(PlayerShieldState(self.entity))

    def update(self, room, entities):
        if check_damage_for_player(self.entity, room.collisions_map.damage_map):
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
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities)


class PlayerPunchState(PlayerState):
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
                if self.entity.current_item.view.copied_animation is not None:
                    room.collisions_map.add_damage(self.entity.current_item.physic.attack_physic, id(self.entity.current_item.physic.attack_physic))
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
        if self.entity.current_item.view.copied_animation is not None:
            if self.entity.current_item.view.copied_animation.done:
                self.finished = True
                room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
                self.entity.states_stack.pop()
                self.entity.states_stack.peek().handle_inputs(self.events, room)
        else:
            self.finished = True
            room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self):
        self.entity.view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_item.view.copied_animation.render(self.entity.view.surface)


class InventoryOpen(PlayerState):
    def __init__(self, entity):
        super().__init__(entity)

    def handle_input(self, event, room):
        pass

    def update(self, room, entities):
        pass

    def draw(self):
        pass