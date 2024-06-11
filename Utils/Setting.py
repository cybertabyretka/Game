import pygame as pg

from Utils.Image import load_image

from Views.Display import Display


DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 700
DISPLAY_NAME = 'DUNGEON'

DISPLAY = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME)

BASE_PATH = 'C:/Users/333/PycharmProjects/Game/'
FONT_PATH = BASE_PATH + 'Data/Fonts/ofont.ru_Hero.ttf'

BACKGROUND_PICTURE = load_image(BASE_PATH + 'Data/Images/MainMenu/background.png')

TILES_SIZE = (35, 35)

NEIGHBOUR_OFFSETS = {'up': (0, -1), 'left': (-1, 0), 'center': (0, 0),
                     'right': (1, 0), 'down': (0, 1), 'left_up': (-1, -1),
                     'right_up': (1, -1), 'left_down': (-1, 1), 'right_down': (1, 1)}

GREEN_RGB = (0, 255, 0)
RED_RGB = (255, 0, 0)
WHITE_RGB = (0, 0, 0)
GRAY_RGB = (122, 122, 122)


def get_font(font_path, font_size):
    return pg.font.Font(font_path, font_size)