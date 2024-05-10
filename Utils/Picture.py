import pygame as pg
import os
import numpy as np
from PIL import Image


class Picture:
    def __init__(self, image: pg.Surface, array):
        self.surface = image
        self.array = array
        self.rotation = 0

    def rotate(self, new_rotation):
        if new_rotation != self.rotation:
            rotation = (new_rotation - self.rotation) // 90
            if rotation < 0:
                rotation += (360 // 90)
            np.rot90(self.array, rotation, (0, 1))
        self.rotation = new_rotation


def load_image(path, set_colour=False, colour_to_change=(0, 0, 0)):
    image = pg.image.load(path).convert()
    array = np.asarray(Image.open(path))
    print(array)
    if set_colour:
        image.set_colorkey(colour_to_change)
    return Picture(image, array)


def load_images(path, set_colour=False, colour_to_change=(0, 0, 0)):
    images = []
    for image_name in sorted(os.listdir(path)):
        images.append(load_image(path + '/' + image_name, set_colour, colour_to_change))
    return images
