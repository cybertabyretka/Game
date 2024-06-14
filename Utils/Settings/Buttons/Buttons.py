from Models.Button import make_button

from Utils.Settings.Colours import GRAY_RGB, WHITE_RGB, RED_RGB, DARK_RED_RGB
from Utils.Settings.Paths import FONT_PATH
from Utils.Settings.Buttons.ButtonsTexts import START, EXIT, SWITCH_SHIELDS, SWITCH_WEAPONS


MAIN_MENU_START_BUTTON = make_button(300, 300, 100, 50, 1, GRAY_RGB, WHITE_RGB, START, WHITE_RGB, 20, FONT_PATH)
MAIN_MENU_EXIT_BUTTON = make_button(300, 350, 100, 50, 1, GRAY_RGB, WHITE_RGB, EXIT, WHITE_RGB, 20, FONT_PATH)

SWORD_CHANGE_BUTTON = make_button(0, 0, 200, 15, 0, DARK_RED_RGB, RED_RGB, SWITCH_WEAPONS, WHITE_RGB, 15, FONT_PATH)
SHIELD_CHANGE_BUTTON = make_button(0, 0, 200, 15, 0, DARK_RED_RGB, RED_RGB, SWITCH_SHIELDS, WHITE_RGB, 15, FONT_PATH)


def get_pressed_button(buttons, mouse_clck_pos):
    for button in buttons:
        if button.view.rect.collidepoint(mouse_clck_pos):
            return button
    return None
