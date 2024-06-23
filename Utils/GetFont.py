import pygame as pg


def get_font(font_path: str, font_size: int) -> pg.font:
    return pg.font.Font(font_path, font_size)
