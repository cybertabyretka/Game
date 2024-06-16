import pickle
import datetime
import time

from Models.Game.Game import Game


def save_game(save, copied_rooms_map, copied_player):
    save.save_time = f'{datetime.date.today()} {time.time()}'
    with open(f'{save.path}rooms_map.pkl', 'wb') as rooms_map_file:
        pickle.dump(copied_rooms_map, rooms_map_file, pickle.HIGHEST_PROTOCOL)
    with open(f'{save.path}player.pkl', 'wb') as player_file:
        pickle.dump(copied_player, player_file, pickle.HIGHEST_PROTOCOL)
    with open('date.txt', 'w') as date_file:
        date_file.write(save.save_time)


def get_game(save, display, entities_surface, rooms_surface):
    with open(f'{save.path}rooms_map.pkl', 'rb') as rooms_map_file:
        rooms_map = pickle.load(rooms_map_file)
    with open(f'{save.path}player.pkl', 'rb') as player_file:
        player = pickle.load(player_file)
    game = Game(display, rooms_map, player, entities_surface, rooms_surface)
    return game
