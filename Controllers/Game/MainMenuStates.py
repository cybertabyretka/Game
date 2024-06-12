import pygame as pg
import pygame.locals as loc

from Controllers.Game.BaseStates import MainMenuState

from Utils.Setting import START, EXIT


class StartState(MainMenuState):
    def __init__(self, main_menu, game):
        super().__init__(main_menu, game)
        self.selected_button = None
        self.any_button_selected = False

    def handle_input(self, event, processes_stack):
        if event.type == pg.QUIT:
            pg.quit()
        if event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            for button in self.main_menu.buttons:
                if button.view.rect.collidepoint(mouse_pos):
                    if self.selected_button is not None and self.selected_button != button:
                        self.selected_button.view.selected = False
                    button.view.selected = True
                    self.selected_button = button
                    self.any_button_selected = True
                    return
                self.any_button_selected = False
        elif event.type == pg.MOUSEBUTTONDOWN:
            click_pos = event.pos
            if self.selected_button is not None and self.selected_button.view.rect.collidepoint(click_pos):
                if self.selected_button.view.text.view.text == START:
                    processes_stack.push(self.game)
                elif self.selected_button.view.text.view.text == EXIT:
                    pg.quit()
        elif event.type == pg.KEYDOWN:
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
            elif event.key == loc.K_RETURN:
                if self.selected_button is not None:
                    if self.selected_button.view.text.view.text == START:
                        processes_stack.push(self.game)
                    elif self.selected_button.view.text.view.text == EXIT:
                        pg.quit()

    def update(self):
        pass

    def draw(self):
        self.main_menu.view.render(self.main_menu.buttons)
        self.main_menu.view.display.update()