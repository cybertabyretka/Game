import pygame as pg

from Constants.Colours import RGB_FOR_BACKGROUND

from Utils.Image import load_image


class BaseProjectileV:
    def __init__(self, image_path: str):
        self.path: str = image_path
        self.image: pg.Surface | None = None

    def download_images(self) -> None:
        self.image = load_image(self.path, True, RGB_FOR_BACKGROUND)

    def draw(self, start_pos: tuple[int, int], surface: pg.Surface) -> None:
        surface.blit(self.image, start_pos)
