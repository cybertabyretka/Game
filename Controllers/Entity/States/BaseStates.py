class PlayerState:
    def __init__(self, entity):
        self.entity = entity
        self.finished = True
        self.events = []

    def handle_input(self, event, room):
        pass

    def handle_inputs(self, events, room):
        for event in events:
            self.handle_input(event, room)

    def update(self, room, entities):
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self):
        self.entity.view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCState:
    def __init__(self, entity):
        self.entity = entity
        self.old_player_center_pos = None
        self.finished = True

    def handle_input(self):
        pass

    def update(self, room, player, entities):
        pass

    def draw(self):
        self.entity.view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))