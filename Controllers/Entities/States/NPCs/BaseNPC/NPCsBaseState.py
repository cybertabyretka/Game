import pygame as pg

from Controllers.Entities.States.AbstractStates.NPCAbstractState import NPCAbstractState

from Models.Entities.BaseEntity import Entity
from Models.Room.Room import Room
from Models.Entities.Player import Player


class NPCBaseState(NPCAbstractState):
    def __init__(self, entity: Entity):
        self.entity: Entity = entity
        self.old_player_center_pos: tuple[int, int] | None = None
        self.finished: bool = True

    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        pass

    def draw(self, surface: pg.Surface) -> None:
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
