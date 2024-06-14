import pygame as pg

from Utils.Image import load_image
from Utils.Settings.Paths import BASE_PATH

from Views.Display import Display


DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 700
DISPLAY_NAME = 'DUNGEON'

DISPLAY = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME)

EMPTY_NAME = 'empty'
EMPTY_SIZE = (20, 20)

BACKGROUND_PICTURE = load_image(BASE_PATH + 'Data/Images/MainMenu/background.png')

TILE_SIZE = (35, 35)

NEIGHBOUR_OFFSETS = {'up': (0, -1), 'left': (-1, 0), 'center': (0, 0),
                     'right': (1, 0), 'down': (0, 1), 'left_up': (-1, -1),
                     'right_up': (1, -1), 'left_down': (-1, 1), 'right_down': (1, 1)}


def get_font(font_path, font_size):
    return pg.font.Font(font_path, font_size)