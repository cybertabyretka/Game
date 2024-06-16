import pygame as pg

pg.init()
pg.font.init()

from Models.Main import Main
from Models.Game.MainMenu import MainMenu


from Utils.Setting import BACKGROUND_PICTURE, DISPLAY, ENTITIES_SURFACE

if __name__ == '__main__':

    main_menu = MainMenu(DISPLAY, BACKGROUND_PICTURE, ENTITIES_SURFACE)
    main = Main(DISPLAY, main_menu)

    main.process.run()
