from Controllers.Entities.States.AbstractStates.PlayerAbstractState import PlayerAbstractState


class PlayerBaseState(PlayerAbstractState):
    def __init__(self, entity):
        self.entity = entity
        self.finished = True
        self.events = []

    def handle_input(self, event, room):
        pass

    def handle_inputs(self, events, room):
        for event in events:
            old_len = self.entity.states_stack.size
            self.handle_input(event, room)
            if self.entity.states_stack.size != old_len:
                self.handle_input(event, room)

    def update(self, room, entities):
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, surface):
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
