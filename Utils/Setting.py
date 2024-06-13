import pygame as pg

from Utils.Image import load_image

from Views.Display import Display


DISPLAY_WIDTH = 700
DISPLAY_HEIGHT = 700
DISPLAY_NAME = 'DUNGEON'

START = 'Start'
EXIT = 'Exit'

DISPLAY = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME)

BASE_PATH = 'C:/Users/333/PycharmProjects/Game/'
FONT_PATH = BASE_PATH + 'Data/Fonts/ofont.ru_Hero.ttf'

EMPTY_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/empty_icon.png', set_colour=True, colour_to_change=(120, 0, 12))
SWORD_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Icon/sword.png', set_colour=True, colour_to_change=(120, 0, 12))
SHIELD_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/Shields/BaseShield/Icon/shield.png', set_colour=True, colour_to_change=(120, 0, 12))

EMPTY_NAME = 'empty'
EMPTY_SIZE = (20, 20)

BACKGROUND_PICTURE = load_image(BASE_PATH + 'Data/Images/MainMenu/background.png')

TILE_SIZE = (35, 35)

NEIGHBOUR_OFFSETS = {'up': (0, -1), 'left': (-1, 0), 'center': (0, 0),
                     'right': (1, 0), 'down': (0, 1), 'left_up': (-1, -1),
                     'right_up': (1, -1), 'left_down': (-1, 1), 'right_down': (1, 1)}

BASE_PLAYER_START_POS = (120, 120)

GREEN_RGB = (0, 255, 0)
RED_RGB = (255, 0, 0)
WHITE_RGB = (0, 0, 0)
GRAY_RGB = (122, 122, 122)
DARK_GRAY_RGB = (75, 75, 75)


def get_font(font_path, font_size):
    return pg.font.Font(font_path, font_size)