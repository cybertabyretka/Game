from Views.Display import Display

from Models.Room.RoomsMap import RoomsMap
from Models.Room.Room import Room
from Models.InteractionObjects.Button import Button


class GameV:
    def __init__(self, display: Display, rooms_map: RoomsMap):
        self.display = display
        self.rooms_map = rooms_map

    def draw(self, room: Room, buttons: list[Button] = None) -> None:
        room.view.render_tile_map(self.display.surface)
        if buttons is not None:
            for button in buttons:
                button.view.draw(self.display.surface)
