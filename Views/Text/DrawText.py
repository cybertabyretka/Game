import pygame as pg

from Utils.GetFont import get_font


def draw_text(surface, text, text_colour, font_size, font_path, start_pos):
    font = get_font(font_path, font_size)
    rendered_text = font.render(text, True, text_colour)
    surface.blit(rendered_text, pg.Rect(start_pos, (0, 0)))