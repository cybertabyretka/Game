import pygame as pg

from Utils.Stack import Stack
from Utils.Draw.Graph.PathFinding import manhattan_distance


def check_damage_map(damage_map, entity_rect):
    damage = 0
    movement = (0, 0)
    for identifier in damage_map:
        damage_rect = damage_map[identifier]
        if entity_rect.colliderect(damage_rect.rect):
            damage += 1
            if damage_rect.direction == 0:
                movement = (0, -entity_rect.width // 2)
            elif damage_rect.direction == 90:
                movement = (entity_rect.width // 2, 0)
            elif damage_rect.direction == 180:
                movement = (0, entity_rect.width // 2)
            else:
                movement = (-entity_rect.width // 2, 0)
    return damage, movement


class State:
    def __init__(self, entity):
        self.entity = entity
        self.finished = True

    def handle_input(self, event, states_stack: Stack, room):
        pass

    def handle_inputs(self, events, states_stack, room):
        for event in events:
            self.handle_input(event, states_stack, room)

    def update(self, room, states_stack, entities):
        pass

    def draw(self, screen):
        self.entity.entity_view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCState:
    def __init__(self, entity):
        self.entity = entity
        self.old_player_center_pos = None
        self.finished = True

    def handle_input(self, states_stack: Stack):
        pass

    def update(self, room, states_stack, player, entities):
        pass

    def draw(self, screen):
        self.entity.entity_view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCAfterPunchState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)
        self.movement = (0, 0)

    def update(self, room, states_stack, player, entities):
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()


class NPCIdleState(NPCState):
    def update(self, room, states_stack, player, entities):
        damage, movement = check_damage_map(room.collisions_map.damage_map, self.entity.physic.collision.rect)
        if damage:
            self.entity.states_stack.push(NPCAfterPunchState(self.entity))
            self.entity.states_stack.peek().movement = movement
        self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y), room.collisions_map.graph)
        self.old_player_center_pos = (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y)
        states_stack.push(NPCWalkState(self.entity))


class PlayerIdleState(State):
    def handle_input(self, event, states_stack, room):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                states_stack.push(PlayerWalkState(self.entity))
        if event.type == pg.MOUSEBUTTONDOWN:
            states_stack.push(PlayerPunchState(self.entity))


class NPCWalkState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)

    def update(self, room, states_stack, player, entities):
        current_player_center_pos = (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y)
        if current_player_center_pos == self.old_player_center_pos and manhattan_distance((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos) > max(player.physic.collision.rect.width, player.physic.collision.rect.height) * 2:
            if self.entity.mind.way:
                next_coord = self.entity.mind.way[0]
                if self.entity.physic.collision.collisions_around['center'].rect.x < next_coord[0]:
                    self.entity.entity_view.rotate(90)
                    self.entity.physic.velocity[0] = self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.x > next_coord[0]:
                    self.entity.entity_view.rotate(270)
                    self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.y < next_coord[1]:
                    self.entity.entity_view.rotate(180)
                    self.entity.physic.velocity[1] = self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.y > next_coord[1]:
                    self.entity.entity_view.rotate(0)
                    self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
                elif self.entity.physic.collision.collisions_around['center'].rect.y == next_coord[1] and self.entity.physic.collision.collisions_around['center'].rect.x == next_coord[0]:
                    self.entity.mind.way.pop(0)
        elif current_player_center_pos != self.old_player_center_pos and manhattan_distance((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos) > max(player.physic.collision.rect.width, player.physic.collision.rect.height) * 2:
            self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos, room.collisions_map.graph)
            self.old_player_center_pos = current_player_center_pos
        else:
            states_stack.pop()
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        entities_around = self.entity.physic.collision.update(self.entity.physic.velocity, entities)
        for direction in entities_around:
            if entities_around[direction] is not None:
                new_state = NPCPunchState(self.entity)
                new_state.direction_for_punch = direction
                states_stack.push(new_state)
                break


class PlayerWalkState(State):
    def __init__(self, entity):
        super().__init__(entity)
        self.directions = set()

    def handle_input(self, event, states_stack, room):
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
            states_stack.push(PlayerPunchState(self.entity))

    def update(self, room, states_stack, entities):
        if len(self.directions) == 0:
            states_stack.pop()
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


class NPCPunchState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)
        self.direction_for_punch = None

    def update(self, room, states_stack, player, entities):
        if self.finished:
            if self.direction_for_punch == 'up':
                self.entity.current_item.set_animation(0, self.entity)
            elif self.direction_for_punch == 'right':
                self.entity.current_item.set_animation(90, self.entity)
            elif self.direction_for_punch == 'down':
                self.entity.current_item.set_animation(180, self.entity)
            else:
                self.entity.current_item.set_animation(270, self.entity)
            room.collisions_map.add_damage(self.entity.current_item.physic.attack_physic, id(self.entity.current_item.physic.attack_physic))
            self.finished = False
        elif self.entity.current_item.weapon_view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
            states_stack.pop()

    def draw(self, screen):
        self.entity.entity_view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_item.weapon_view.copied_animation.render(screen)


class PlayerPunchState(State):
    def __init__(self, entity):
        super().__init__(entity)
        self.events = []

    def handle_input(self, event, states_stack: Stack, room):
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
                    states_stack.pop()
            else:
                self.finished = True
                states_stack.pop()
        elif event.type != pg.MOUSEBUTTONDOWN:
            self.events.append(event)

    def update(self, room, states_stack, entities):
        if self.entity.current_item.weapon_view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
            states_stack.pop()
            states_stack.peek().handle_inputs(self.events, states_stack, room)

    def draw(self, screen):
        self.entity.entity_view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        self.entity.current_item.weapon_view.copied_animation.render(screen)