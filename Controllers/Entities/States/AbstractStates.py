from abc import *


class PlayerAbstractState(ABC):
    @abstractmethod
    def handle_input(self, event, room):
        pass

    @abstractmethod
    def handle_inputs(self, events, room):
        pass

    @abstractmethod
    def update(self, room, entities):
        pass

    @abstractmethod
    def draw(self, surface):
        pass


class NPCAbstractState(ABC):
    @abstractmethod
    def update(self, room, player, entities):
        pass

    @abstractmethod
    def draw(self, surface):
        pass