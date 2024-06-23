import pygame as pg
from abc import *

from Models.Room.Room import Room
from Models.Entities.Player import Player
from Models.Entities.BaseEntity import Entity


class NPCAbstractState(ABC):
    @abstractmethod
    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        pass

    @abstractmethod
    def draw(self, surface: pg.Surface) -> None:
        pass
