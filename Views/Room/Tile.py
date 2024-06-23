import pygame as pg

from Utils.Image import load_image


class TileV:
    def __init__(self, path: str):
        self.path: str = path
        self.image: pg.Surface | None = None

    def download_images(self) -> None:
        if self.path is not None:
            self.image = load_image(self.path)

    def draw(self, surface: pg.Surface, pos: tuple[int, int]) -> None:
        if self.image is not None:
            surface.blit(self.image, pos)
