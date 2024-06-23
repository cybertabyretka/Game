import pygame as pg

from Controllers.Entities.States.AbstractStates.PlayerAbstractState import PlayerAbstractState

from Models.Entities.BaseEntity import Entity
from Models.Room.Room import Room


class PlayerBaseState(PlayerAbstractState):
    def __init__(self, entity: Entity):
        self.entity: Entity = entity
        self.finished: bool = True
        self.events: list[pg.event] = []

    def handle_input(self, event: pg.event, room: Room) -> None:
        pass

    def handle_inputs(self, events: list[pg.event], room: Room) -> None:
        for event in events:
            old_len = self.entity.states_stack.size
            self.handle_input(event, room)
            if self.entity.states_stack.size != old_len:
                self.handle_input(event, room)

    def update(self, room: Room, entities: list[Entity]) -> None:
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, surface: pg.Surface) -> None:
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
