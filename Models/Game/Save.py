import pickle
import os

from Utils.BaseGame import BASE_ROOMS_MAP, BASE_PLAYER

from Models.Game.Game import Game


class Save:
    def __init__(self, file_path):
        self.path = file_path
        if not os.listdir(file_path):
            with open(f'{file_path}rooms_map.pkl', 'wb') as save_file:
                pickle.dump(BASE_ROOMS_MAP, save_file, pickle.HIGHEST_PROTOCOL)
            with open(f'{file_path}player.pkl', 'wb') as save_file:
                pickle.dump(BASE_PLAYER, save_file, pickle.HIGHEST_PROTOCOL)
            with open(f'{file_path}date.txt', 'w') as date_file:
                date_file.write('---------- --:--:--')
                self.save_time = '---------- --:--:--'
        else:
            with open(f'{file_path}date.txt', 'r') as date_file:
                self.save_time = date_file.readline().rstrip()

    def delete(self):
        if os.listdir(self.path):
            if os.path.exists(f'{self.path}rooms_map.pkl'):
                os.remove(f'{self.path}rooms_map.pkl')
            if os.path.exists(f'{self.path}player.pkl'):
                os.remove(f'{self.path}player.pkl')
            if os.path.exists(f'{self.path}date.txt'):
                os.remove(f'{self.path}date.txt')