import pygame as pg

from Models.AppStates.Game import Game
from Models.Save import Save

from Views.Display import Display


def get_game(save: Save, display: Display, entities_surface: pg.Surface, rooms_surface: pg.Surface, auto_saves: list[Save], saves: list[Save]) -> Game:
    rooms_map = save.get_rooms_map()
    player = save.get_player()
    game = Game(display, rooms_map, player, entities_surface, rooms_surface, auto_saves, saves)
    game.after_load_preprocess()
    return game
