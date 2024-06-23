from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState


class PlayerAfterPunchState(PlayerBaseState):
    def __init__(self, entity, movement, damage):
        super().__init__(entity)
        self.movement = movement
        self.damage = damage

    def handle_input(self, event, room):
        if len(self.events) < 35:
            self.events.append(event)

    def update(self, room, entities):
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage_types[damage_type]
        self.entity.health.health -= damage
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()
        self.entity.states_stack.peek().handle_inputs(self.events, room)