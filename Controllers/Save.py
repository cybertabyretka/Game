from shelve import open as open_sh
import datetime
import time

from Utils.BaseGame import BASE_GAME


def save_game(path, game):
    with open_sh(path) as save_file:
        save_file['game'] = game
        save.date = {'date': str(datetime.date.today()),
                     'time': str(time.time())}


def get_game(path):
    with open_sh(path) as save_file:
         if save_file['game'] is None:
            return BASE_GAME
         return save_file['game']