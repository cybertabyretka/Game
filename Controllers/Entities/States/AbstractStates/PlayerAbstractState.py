import pygame as pg
from abc import *

from Models.Room.Room import Room


class PlayerAbstractState(ABC):
    @abstractmethod
    def handle_input(self, event: pg.event, room: Room) -> None:
        pass

    @abstractmethod
    def handle_inputs(self, events: list[pg.event], room: Room) -> None:
        pass

    @abstractmethod
    def update(self, room: Room, entities) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pg.Surface) -> None:
        pass
