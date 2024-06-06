import pygame as pg

from Controllers import Game_to_del
from Views import Display
pg.init()
pg.font.init()


if __name__ == '__main__':
    width, height, name = 700, 700, 'Dungeon'
    game = Game_to_del.Game(Display.Display(width, height, name))
    game.run()
