import pygame as pg

from Views.Display import Display

from Models.InteractionObjects.Button import Button


class MainMenuV:
    def __init__(self, display: Display, background_surface: pg.Surface):
        self.display: Display = display
        self.background_surface: pg.Surface = background_surface

    def draw(self, buttons: list[Button]) -> None:
        self.display.surface.blit(self.background_surface, (0., 0.))
        for button in buttons:
            button.view.draw(self.display.surface)
