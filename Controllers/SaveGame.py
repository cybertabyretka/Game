import pickle
import datetime


def save_game(save, copied_rooms_map, copied_player):
    save.save_time = f'{datetime.datetime.now()}'
    with open(f'{save.path}rooms_map.pkl', 'wb') as rooms_map_file:
        pickle.dump(copied_rooms_map, rooms_map_file, pickle.HIGHEST_PROTOCOL)
    with open(f'{save.path}player.pkl', 'wb') as player_file:
        pickle.dump(copied_player, player_file, pickle.HIGHEST_PROTOCOL)
    with open(f'{save.path}date.txt', 'w') as date_file:
        date_file.write(save.save_time)