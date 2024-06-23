from Models.Room.Door import Door
from Models.Room.Room import Room

from Controllers.RoomMap.RoomsMapUtils import connect_rooms


class RoomsMap:
    def __init__(self, size: tuple[int, int], current_index: tuple[int, int] = (0, 0)):
        self.size: tuple[int, int] = size
        self.map: list[list[None | Room]] = [[None for _ in range(size[1])] for _ in range(size[0])]
        self.current_index: tuple[int, int] = current_index
        self.doors_connections: dict[Door, list[Room]] = {}

    def get_current_room(self) -> None:
        return self.map[self.current_index[0]][self.current_index[1]]

    def new_object_preprocess(self, doors_connections: dict[Door, list[Room]]) -> None:
        self.download_images()
        self.add_doors_connections(doors_connections)
        self.add_doors()

    def after_load_preprocess(self) -> None:
        self.download_images()

    def add_doors_connections(self, doors_connections: dict[Door, list[Room]]) -> None:
        self.doors_connections = doors_connections

    def add_doors(self) -> None:
        for door in self.doors_connections:
            door.add_rooms(self.doors_connections[door][0], self.doors_connections[door][1])
        connect_rooms(list(self.doors_connections.keys()))

    def copy_for_save(self, current_room: Room):
        new_rooms = {}
        copied_map = RoomsMap(self.size)
        copied_doors_connections = {}
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.map[i][j] is not None:
                    copied_map.map[i][j] = self.map[i][j].copy_for_save()
                    new_rooms[self.map[i][j]] = copied_map.map[i][j]
                    if self.map[i][j] == current_room:
                        copied_map.current_index = (i, j)
        for door in self.doors_connections:
            copied_rooms = []
            for room in self.doors_connections[door]:
                copied_rooms.append(new_rooms[room])
            copied_doors_connections[door.copy_for_save()] = copied_rooms
        copied_map.add_doors_connections(copied_doors_connections)
        copied_map.add_doors()
        return copied_map

    def download_images(self) -> None:
        for door in self.doors_connections:
            door.download_images()
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                if self.map[i][j] is not None:
                    self.map[i][j].download_images()
