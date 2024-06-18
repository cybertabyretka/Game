import pickle
import datetime


def save_game(save, copied_rooms_map, copied_player):
    date = str(datetime.datetime.now())[:19]
    save.set_rooms_map(copied_rooms_map)
    save.set_player(copied_player)
    save.set_date(date)