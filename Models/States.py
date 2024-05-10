import pygame as pg
from Utils.Stack import Stack


class State:
    def __init__(self, player):
        self.player = player

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
                states_stack.push(PlayerWalkState(self.player))

    def draw(self, screen):
        self.player.entity_view.render(screen, (self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))


class PlayerWalkState(State):
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
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                print(f'kw: {self.directions}')
                print(f'kw: {pg.K_w}')
                self.player.physic.velocity[1] = 0
                self.directions.remove(pg.K_w)
            if event.key == pg.K_s:
                print(f'ks: {self.directions}')
                print(f'ks: {pg.K_s}')
                self.player.physic.velocity[1] = 0
                self.directions.remove(pg.K_s)
            if event.key == pg.K_a:
                print(f'ka: {self.directions}')
                print(f'ka: {pg.K_a}')
                self.player.physic.velocity[0] = 0
                self.directions.remove(pg.K_a)
            if event.key == pg.K_d:
                print(f'kd: {self.directions}')
                print(f'kd: {pg.K_d}')
                self.player.physic.velocity[0] = 0
                self.directions.remove(pg.K_d)
        if len(self.directions) == 0:
            states_stack.pop()

    def update(self, room):
        for direction in self.directions:
            if direction == pg.K_w:
                self.player.physic.velocity[1] = -self.player.physic.max_velocity
            elif direction == pg.K_s:
                self.player.physic.velocity[1] = self.player.physic.max_velocity
            elif direction == pg.K_a:
                self.player.physic.velocity[0] = -self.player.physic.max_velocity
            elif direction == pg.K_d:
                self.player.physic.velocity[0] = self.player.physic.max_velocity
        self.player.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.player.physic.collision.update(self.player.physic.velocity)

    def draw(self, screen):
        self.player.entity_view.clear_surface(screen)
        self.player.entity_view.render(screen, (self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))