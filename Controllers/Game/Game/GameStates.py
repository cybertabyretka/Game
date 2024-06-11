from Controllers.Game.BaseStates import GameState


class GameOn(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event):
        if event.type == pg.QUIT:
            self.game.is_running = False
        old_len = self.game.player.states_stack.size()
        self.game.player.states_stack.peek().handle_input(event, self.game.base_room)
        if self.game.player.states_stack.size() != old_len:
            self.game.player.states_stack.peek().handle_input(event, self.game.base_room)

    def update(self):
        self.game.player.states_stack.peek().update(self.game.base_room, self.game.entities)
        for NPC in self.game.NPCs:
            NPC.states_stack.peek().update(self.game.base_room, self.game.player, self.game.entities)

    def draw(self):
        self.game.base_room.room_view.render_tile_map(self.game.base_room.room_view.surface)
        self.game.base_room.room_view.surface.blit(self.game.player.entity_view.surface, (0., 0.))
        self.game.display.surface.blit(self.game.base_room.room_view.surface, (self.game.base_room.room_view.surface.get_rect().x, self.game.base_room.room_view.surface.get_rect().y))