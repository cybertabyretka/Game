import sys

import pygame as pg

from Controllers.Game.BaseStates import GameState
from Controllers.Entity.States.PlayerStates import InventoryOpenState, PlayerStealState

from Views.Entity.Entity import render_entities
from Views.Entity.HealthBar import render_health_bars

from Utils.DistanceCounting import manhattan_distance


class Running(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                if not self.game.room.live_NPCs_count:
                    for door in self.game.room.collisions_map.doors:
                        if door.current_tile.collision.rect.collidepoint(pg.mouse.get_pos()):
                            if manhattan_distance(door.current_tile.collision.rect.center, self.game.player.physic.collision.rect.center) <= min(self.game.player.physic.collision.rect.width, self.game.player.physic.collision.rect.height) * 2:
                                self.game.room, self.game.player.physic.collision.rect.topleft = door.get_next_room(self.game.room)
            elif event.key == pg.K_p:
                self.game.states_stack.push(OnPause(self.game))
                self.game.states_stack.peek().handle_input(event, processes_stack, main_process)
                return
            elif event.key == pg.K_e:
                old_len = self.game.player.states_stack.size
                self.game.player.states_stack.peek().handle_input(event, self.game.room)
                if self.game.player.states_stack.size() != old_len:
                    self.game.states_stack.push(OnPause(self.game))
                    self.game.states_stack.peek().handle_input(event, processes_stack, main_process)
                    return
        old_len = self.game.player.states_stack.size()
        self.game.player.states_stack.peek().handle_input(event, self.game.room)
        if self.game.player.states_stack.size() != old_len:
            self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self):
        self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)
        for NPC in self.game.room.NPCs:
            NPC.states_stack.peek().update(self.game.room, self.game.player, [*self.game.room.NPCs, self.game.player])

    def draw(self):
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        render_entities(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        render_health_bars(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        self.game.view.display.update()


class OnPause(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                if type(self.game.player.states_stack.peek()) not in [InventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
            elif event.key == pg.K_e:
                if type(self.game.player.states_stack.peek()) in [InventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
        self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self):
        if self.finished:
            self.game.states_stack.pop()
        else:
            self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)

    def draw(self):
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        self.game.player.states_stack.peek().draw(self.game.entities_surface)
        self.game.view.display.update()