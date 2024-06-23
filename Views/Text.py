import pygame as pg

from Utils.GetFont import get_font


class TextV:
    def __init__(self, text: str, text_colour: tuple[int ,int, int], font_size: int, font_path: str):
        self.text: str = text
        self.colour: tuple[int, int, int] = text_colour
        self.font_size: int = font_size
        self.font_path: str = font_path

    def change_font(self, font_size: int = None, font_path: str = None) -> None:
        if font_size is not None:
            self.font_size = font_size
        if font_path is not None:
            self.font_path = font_path

    def draw(self, surface: pg.Surface, rect: pg.Rect) -> None:
        rendered_text = get_font(self.font_path, self.font_size).render(self.text, True, self.colour)
        surface.blit(rendered_text, rect)
