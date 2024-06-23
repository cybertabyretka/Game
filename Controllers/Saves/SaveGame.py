import datetime

from Models.Save import Save
from Models.Room.RoomsMap import RoomsMap
from Models.Entities.Player import Player


def save_game(save: Save, copied_rooms_map: RoomsMap, copied_player: Player) -> None:
    date = str(datetime.datetime.now())[:19]
    save.set_rooms_map(copied_rooms_map)
    save.set_player(copied_player)
    save.set_date(date)
