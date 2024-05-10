import pygame as pg


class State:
    def __init__(self, player):
        self.player = player

    def handle_input(self, event):
        pass

    def update(self, room):
        pass

    def draw(self, screen):
        pass


class EntityIdleState(State):
    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                self.__class__ = PlayerWalkState(self.player)
                self.handle_input(event)

    def draw(self, screen):
        self.player.entity_view.render(screen, (self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))


class PlayerWalkState(State):
    def handle_input(self, event):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.player.physic.velocity[1] -= self.player.physic.max_velocity
            if event.key == pg.K_s:
                self.player.physic.velocity[1] += self.player.physic.max_velocity
            if event.key == pg.K_a:
                self.player.physic.velocity[0] -= self.player.physic.max_velocity
            if event.key == pg.K_d:
                self.player.physic.velocity[0] += self.player.physic.max_velocity
        if event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.player.physic.velocity[1] += self.player.physic.max_velocity
            if event.key == pg.K_s:
                self.player.physic.velocity[1] -= self.player.physic.max_velocity
            if event.key == pg.K_a:
                self.player.physic.velocity[0] += self.player.physic.max_velocity
            if event.key == pg.K_d:
                self.player.physic.velocity[0] -= self.player.physic.max_velocity
        if self.player.physic.velocity[0] == 0 and self.player.physic.velocity[1] == 0:
            self.__class__ = EntityIdleState(self.player)

    def update(self, room):
        self.player.physic.collision.get_collisions_around(room.collisions_map.map, room.room_view.tile_size)
        self.player.physic.collision.update(self.player.physic.velocity)

    def draw(self, screen):
        self.player.entity_view.render(screen, (self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))