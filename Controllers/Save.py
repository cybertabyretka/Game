import pickle
import datetime
import time

from Utils.BaseGame import copy_base_game


def save_game(save, game):
    save.save_time = f'{datetime.date.today()} {time.time()}'
    with open_sh(save.path, 'wb') as save_file:
        pickle.dump(game, save_file, pickle.HIGHEST_PROTOCOL)
    with open('date.txt', 'w') as date_file:
        date_file.writelines([save.save_time])


def get_game(save):
    with open_sh(save.path) as save_file:
         if save_file['game'] is not None:
            return save_file['game']
    new_game = copy_base_game()
    save_game(save, new_game)
    return new_game
