import pygame as pg

from Constants.Mouse import MOUSE_BUTTONS_NUMBER


def check_left_mouse_button() -> bool:
    return pg.mouse.get_pressed(MOUSE_BUTTONS_NUMBER)[0]


def check_right_mouse_button() -> bool:
    return pg.mouse.get_pressed(MOUSE_BUTTONS_NUMBER)[2]
