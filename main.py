import pygame as pg

import Controller
import Model
import View
pg.init()


if __name__ == '__main__':
    width, height, name = 700, 700, 'Dungeon'
    game = Controller.Game(View.Display(width, height, name))
    game.run()
