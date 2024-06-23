import pygame as pg
from collections.abc import Iterable

from Utils.GetFont import get_font


def draw_text(surface: pg.Surface, text: str, text_colour: tuple[int, int, int], font_size: int, font_path: str, start_pos: Iterable[int]) -> None:
    start_pos = tuple(start_pos)
    font = get_font(font_path, font_size)
    rendered_text = font.render(text, True, text_colour)
    surface.blit(rendered_text, pg.Rect(start_pos, (0, 0)))
