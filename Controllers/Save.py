import pickle
import datetime
import time

from Utils.BaseGame import get_base_game


def save_game(save, game):
    save.save_time = f'{datetime.date.today()} {time.time()}'
    with open_sh(save.path, 'wb') as save_file:
        pickle.dump(game, save_file, pickle.HIGHEST_PROTOCOL)
    with open('date.txt', 'w') as date_file:
        date_file.writelines([save.save_time])


def get_game(save, display, entities_surface):
    with open_sh(save.path) as save_file:
         if save_file['game'] is not None:
            return save_file['game']
    new_game = get_base_game(display, entities_surface)
    save_game(save, new_game)
    return new_game
