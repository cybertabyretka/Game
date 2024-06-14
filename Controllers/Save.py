from shelve import open as open_sh
import datetime
import time


def save_game(save, game):
    with open_sh(save.file_path) as save_file:
        save_file['game'] = game
        save.date = {'date': str(datetime.date.today()),
                     'time': str(time.time())}


def get_game(save):
    with open_sh(save.file_path) as save_file:
        return save_file['game']