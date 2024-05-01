import pygame as pg


class Display:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.display = pg.display
        self.screen = self.display.set_mode((width, height))
        self.display.set_caption(name)
        self.name = name

    def update(self):
        self.display.flip()

    def draw_img(self, img, pos):
        self.screen.blit(img, pos)