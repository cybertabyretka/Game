import pygame as pg
import os
from PIL import Image


def load_image(path: str, set_colour: bool = False, colour_to_change: tuple[int, int, int] = (0, 0, 0)) -> pg.Surface:
    image = pg.image.load(path).convert()
    if set_colour:
        image.set_colorkey(colour_to_change)
    return image


def load_images(path: str, set_colour: bool = False, colour_to_change: tuple[int, int, int] = (0, 0, 0)) -> list[pg.Surface]:
    images = []
    for image_name in sorted(os.listdir(path)):
        images.append(load_image(path + '/' + image_name, set_colour, colour_to_change))
    return images


def resize_image(path: str, new_path: str, new_size: tuple[int, int]) -> None:
    image = Image.open(path)
    image = image.resize(new_size)
    image.save(new_path)
