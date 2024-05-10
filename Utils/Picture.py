import pygame as pg
import os


def load_image(path, set_colour=False, colour_to_change=(0, 0, 0)):
    image = pg.image.load(path).convert()
    if set_colour:
        image.set_colorkey(colour_to_change)
    return image


def load_images(path, set_colour=False, colour_to_change=(0, 0, 0)):
    images = []
    for image_name in sorted(os.listdir(path)):
        images.append(load_image(path + '/' + image_name, set_colour, colour_to_change))
    return images
