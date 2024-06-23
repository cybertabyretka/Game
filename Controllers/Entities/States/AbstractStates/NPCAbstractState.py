import pygame as pg
from abc import *

from Models.Room.Room import Room


class NPCAbstractState(ABC):
    @abstractmethod
    def update(self, room: Room, player, entities) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pg.Surface) -> None:
        pass
