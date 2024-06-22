import pygame as pg

pg.init()
pg.font.init()

from Models.Main import Main
from Models.AppStates.MainMenu import MainMenu

from BaseVariables.Display import DISPLAY, ENTITIES_SURFACE, ROOMS_SURFACE
from BaseVariables.Others import BACKGROUND_PICTURE

if __name__ == '__main__':
    main_menu = MainMenu(DISPLAY, BACKGROUND_PICTURE, ENTITIES_SURFACE, ROOMS_SURFACE)
    main = Main(DISPLAY, main_menu)
    main.process.run()
