import pygame as pg

from Utils.Image import load_image

from BaseVariables.Paths import BASE_PATH


EMPTY_NAME: str = 'empty'
EMPTY_SIZE: tuple[int, int] = (20, 20)

BACKGROUND_PICTURE: pg.Surface = load_image(BASE_PATH + 'ReadyData/Images/MainMenu/background.png')

TILE_SIZE: tuple[int, int] = (35, 35)