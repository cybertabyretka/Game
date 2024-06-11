import pygame as pg

from Controllers import Game_to_del

from Views.Display import Display

from Models.Main import Main
from Models.Game.Game import Game
from Models.Game.MainMenu import MainMenu

from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME

pg.init()
pg.font.init()


if __name__ == '__main__':
    display = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME)
    game = Game()
    main_menu = MainMenu()
    main = Main(display, main_menu, game)
    main.process.run()
