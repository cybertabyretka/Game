import pygame as pg
from abc import *

from Models.Room.Room import Room
from Models.Entities.BaseEntity import Entity


class PlayerAbstractState(ABC):
    @abstractmethod
    def handle_input(self, event: pg.event, room: Room) -> None:
        pass

    @abstractmethod
    def handle_inputs(self, events: list[pg.event], room: Room) -> None:
        pass

    @abstractmethod
    def update(self, room: Room, entities: list[Entity]) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pg.Surface) -> None:
        pass
