import pickle

from Models.Game.Game import Game


def get_game(save, display, entities_surface, rooms_surface, auto_saves, saves):
    with open(f'{save.path}rooms_map.pkl', 'rb') as rooms_map_file:
        rooms_map = pickle.load(rooms_map_file)
    with open(f'{save.path}player.pkl', 'rb') as player_file:
        player = pickle.load(player_file)
    game = Game(display, rooms_map, player, entities_surface, rooms_surface, auto_saves, saves)
    game.after_load_preprocess()
    return game
