import pygame as pg

from Utils.GetFont import get_font


def draw_text(surface: pg.Surface, text: str, text_colour: tuple[int, int, int], font_size: int, font_path: str, start_pos: tuple[int, int, int]) -> None:
    font = get_font(font_path, font_size)
    rendered_text = font.render(text, True, text_colour)
    surface.blit(rendered_text, pg.Rect(start_pos, (0, 0)))
