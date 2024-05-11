import pygame as pg
from Utils.Stack import Stack


class State:
    def __init__(self, player):
        self.player = player
        self.finished = True

    def handle_input(self, event, states_stack: Stack):
        pass

    def update(self, room):
        pass

    def draw(self, screen):
        pass


class EntityIdleState(State):
    def handle_input(self, event, states_stack):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                states_stack.push(EntityWalkState(self.player))
        if event.type == pg.MOUSEBUTTONDOWN:
            states_stack.push(EntityPunchState(self.player))

    def draw(self, screen):
        self.player.entity_view.render((self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))


class EntityWalkState(State):
    def __init__(self, player):
        super().__init__(player)
        self.directions = set()

    def handle_input(self, event, states_stack):
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
                self.player.physic.velocity[1] = 0
                self.directions.remove(pg.K_w)
            if event.key == pg.K_s:
                self.player.physic.velocity[1] = 0
                self.directions.remove(pg.K_s)
            if event.key == pg.K_a:
                self.player.physic.velocity[0] = 0
                self.directions.remove(pg.K_a)
            if event.key == pg.K_d:
                self.player.physic.velocity[0] = 0
                self.directions.remove(pg.K_d)
        if len(self.directions) == 0:
            states_stack.pop()
        if event.type == pg.MOUSEBUTTONDOWN:
            states_stack.push(EntityPunchState(self.player))

    def update(self, room):
        for direction in self.directions:
            if direction == pg.K_w:
                self.player.entity_view.rotate(0)
                self.player.physic.velocity[1] = -self.player.physic.max_velocity
            elif direction == pg.K_s:
                self.player.entity_view.rotate(180)
                self.player.physic.velocity[1] = self.player.physic.max_velocity
            elif direction == pg.K_a:
                self.player.entity_view.rotate(270)
                self.player.physic.velocity[0] = -self.player.physic.max_velocity
            elif direction == pg.K_d:
                self.player.entity_view.rotate(90)
                self.player.physic.velocity[0] = self.player.physic.max_velocity
        self.player.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.player.physic.collision.update(self.player.physic.velocity)

    def draw(self, screen):
        self.player.entity_view.clear_surface()
        self.player.entity_view.render((self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))


class EntityPunchState(State):
    def __init__(self, player):
        super().__init__(player)

    def handle_input(self, event, states_stack: Stack):
        if self.finished:
            direction_for_punch = None
            if pg.mouse.get_pressed(3)[0]:
                for direction in self.player.physic.collision.collisions_around:
                    if self.player.physic.collision.collisions_around[direction].rect.collidepoint(event.pos):
                        direction_for_punch = direction
                        break
            if direction_for_punch is not None:
                if direction_for_punch == 'up':
                    self.player.current_item.weapon_view.set_animation(0, self.player)
                elif direction_for_punch == 'right':
                    self.player.current_item.weapon_view.set_animation(90, self.player)
                elif direction_for_punch == 'down':
                    self.player.current_item.weapon_view.set_animation(180, self.player)
                elif direction_for_punch == 'left':
                    self.player.current_item.weapon_view.set_animation(270, self.player)
                if self.player.current_item.weapon_view.copied_animation is not None:
                    self.finished = False
                else:
                    self.finished = True
                    states_stack.pop()
            else:
                self.finished = True
                states_stack.pop()
        else:
            if self.player.current_item.weapon_view.copied_animation.done:
                self.finished = True
                states_stack.pop()

    def update(self, room):
        self.draw(self.player.entity_view.surface)

    def draw(self, screen):
        self.player.entity_view.clear_surface()
        self.player.entity_view.render((self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))
        self.player.current_item.weapon_view.copied_animation.render(screen)