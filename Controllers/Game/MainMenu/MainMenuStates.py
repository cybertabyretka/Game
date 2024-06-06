import pygame as pg
import pygame.locals as loc

from Controllers.Game.BaseStates import MainMenuState


class StartState(MainMenuState):
    def __init__(self, main_menu):
        super().__init__(main_menu)
        self.selected_button = None
        self.any_button_selected = False

    def handle_input(self, event):
        for event in pg.event.get():
            if event.type == pg.MOUSEMOTION:
                mouse_click_pos = event.pos
                for button in self.main_menu.buttons:
                    if button.view.rect.coolidepoint(mouse_click_pos):
                        if self.selected_button is not None or self.selected_button != button:
                            self.selected_button.view.selected = False
                        button.view.selected = True
                        self.any_button_selected = True
                        return
                    self.any_button_selected = False
            elif event.type == pg.MOUSEBUTTONDOWN:
                if event.key == loc.K_s or event.key == loc.K_DOWN:
                    if self.selected_button is not None:
                        self.selected_button.view.selected = False
                        current_button_index = self.main_menu.buttons.index(self.selected_button)
                        self.selected_button = self.main_menu.buttons[(current_button_index + 1) % len(self.main_menu.buttons)]
                    else:
                        self.selected_button = self.main_menu.buttons[0]
                    self.selected_button.view.selected = True
                elif event.key == loc.K_w or event.key == loc.K_UP:
                    if self.selected_button is not None:
                        self.selected_button.view.selected = False
                        current_button_index = self.main_menu.buttons.index(self.selected_button)
                        self.selected_button = self.main_menu.buttons[(current_button_index - 1) % len(self.main_menu.buttons)]
                    else:
                        self.selected_button = self.main_menu.buttons[0]
                    self.selected_button.view.selected = True

    def update(self):
        pass

    def draw(self):
        self.main_menu.view.render(self.main_menu.buttons)