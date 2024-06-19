import pickle

from Models.Game.Game import Game


def get_game(save, display, entities_surface, rooms_surface, auto_saves, saves):
    rooms_map = save.get_rooms_map()
    player = save.get_player()
    game = Game(display, rooms_map, player, entities_surface, rooms_surface, auto_saves, saves)
    game.after_load_preprocess()
    return game
