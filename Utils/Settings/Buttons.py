from Models.Button import make_button

from Utils.Settings.Colours import GRAY_RGB, WHITE_RGB, RED_RGB, DARK_RED_RGB
from Utils.Settings.Paths import FONT_PATH


MAIN_MENU_START_BUTTON = make_button(300, 300, 100, 50, 1, GRAY_RGB, WHITE_RGB, 'Start', WHITE_RGB, 20, FONT_PATH)
MAIN_MENU_EXIT_BUTTON = make_button(300, 350, 100, 50, 1, GRAY_RGB, WHITE_RGB, 'Exit', WHITE_RGB, 20, FONT_PATH)

SWORD_CHANGE_BUTTON = make_button(0, 0, 200, 15, 0, DARK_RED_RGB, RED_RGB, 'Make it a current weapon', WHITE_RGB, 15, FONT_PATH)
SHIELD_CHANGE_BUTTON = make_button(0, 0, 200, 15, 0, DARK_RED_RGB, RED_RGB, 'Make it a current shield', WHITE_RGB, 15, FONT_PATH)