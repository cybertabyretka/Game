import pygame as pg

from Controllers import Game
from Views import Display

pg.init()


if __name__ == '__main__':
    width, height, name = 700, 700, 'Dungeon'
    game = Controller.Game(View.Display(width, height, name))
    game.run()
