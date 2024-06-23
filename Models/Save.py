import os
import pickle

from BaseVariables.Game import BASE_ROOMS_MAP, BASE_PLAYER

from Models.Room.RoomsMap import RoomsMap
from Models.Entities.Player import Player

from Constants.Date import *


class Save:
    def __init__(self, file_path: str):
        self.path: str = file_path
        if not os.listdir(file_path):
            self.set_rooms_map(BASE_ROOMS_MAP)
            self.set_player(BASE_PLAYER)
            self.set_date(f'{BASE_DATE} {BASE_TIME}')
        else:
            self.save_time: str = self.get_date()

    def get_date_and_time_as_tuples(self) -> None | tuple[tuple[int, ...], tuple[int, ...]]:
        if self.save_time.split()[0] != BASE_DATE and self.save_time.split()[1] != BASE_TIME:
            date, time = self.get_date().split()
            date, time = tuple(reversed(list(map(int, date.split('-'))))), tuple(reversed(list(map(int, time.split(':')))))
            return date, time

    def set_rooms_map(self, copied_rooms_map: RoomsMap) -> None:
        with open(f'{self.path}rooms_map.pkl', 'wb') as room_map_file:
            pickle.dump(copied_rooms_map, room_map_file, pickle.HIGHEST_PROTOCOL)

    def set_player(self, copied_player: Player) -> None:
        with open(f'{self.path}player.pkl', 'wb') as player_file:
            pickle.dump(copied_player, player_file, pickle.HIGHEST_PROTOCOL)

    def set_date(self, date: str) -> None:
        with open(f'{self.path}date.txt', 'w') as date_file:
            date_file.write(date)
            self.save_time = date

    def get_rooms_map(self) -> RoomsMap:
        with open(f'{self.path}rooms_map.pkl', 'rb') as room_map_file:
            return pickle.load(room_map_file)

    def get_player(self) -> Player:
        with open(f'{self.path}player.pkl', 'rb') as player_file:
            return pickle.load(player_file)

    def get_date(self) -> str:
        with open(f'{self.path}date.txt', 'r') as date_file:
            return date_file.readline().rstrip()

    def delete(self) -> None:
        if os.listdir(self.path):
            if os.path.exists(f'{self.path}rooms_map.pkl'):
                os.remove(f'{self.path}rooms_map.pkl')
            if os.path.exists(f'{self.path}player.pkl'):
                os.remove(f'{self.path}player.pkl')
            if os.path.exists(f'{self.path}date.txt'):
                os.remove(f'{self.path}date.txt')