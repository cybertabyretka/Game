import pygame as pg

from Controllers.Game.BaseStates import GameState

from Views.Entity.Entity import render_entities
from Views.Entity.HealthBar import render_health_bars


class GameOn(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event, processes_stack):
        if event.type == pg.QUIT:
            pg.quit()
        old_len = self.game.player.states_stack.size()
        self.game.player.states_stack.peek().handle_input(event, self.game.room)
        if self.game.player.states_stack.size() != old_len:
            self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self):
        self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)
        for NPC in self.game.room.NPCs:
            NPC.states_stack.peek().update(self.game.room, self.game.player, [*self.game.room.NPCs, self.game.player])

    def draw(self):
        self.game.room.view.render_tile_map(self.game.room.view.surface)
        self.game.room.view.surface.blit(self.game.player.view.surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.room.view.surface, (self.game.room.view.surface.get_rect().x, self.game.room.view.surface.get_rect().y))
        render_entities(self.game.room.NPCs, self.game.player, self.game.player.view.surface)
        render_health_bars(self.game.room.NPCs, self.game.player, self.game.player.view.surface)
        self.game.view.display.update()