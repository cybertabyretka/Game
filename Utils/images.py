import pygame as pg


def load_image(path, set_colour=False, colour_to_change=(0, 0, 0)):
    image = pg.image.load(path).convert()
    if set_colour:
        image.set_colorkey(colour_to_change)
    return image