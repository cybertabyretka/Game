import sys

import pygame as pg
import pygame.locals as loc

from Controllers.Game.BaseStates import MainMenuState

from Utils.Settings.Buttons.ButtonsTexts import START, EXIT, SELECT_1, SELECT_2, SELECT_3, SELECT_4, SELECT_5, SELECT_1_AUTO, SELECT_2_AUTO, SELECT_3_AUTO, SELECT_4_AUTO, SELECT_5_AUTO


class StartState(MainMenuState):
    def __init__(self, main_menu, game, buttons):
        super().__init__(main_menu, game, buttons)
        self.selected_button = None

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            for button in self.buttons:
                if button.view.rect.collidepoint(mouse_pos):
                    if self.selected_button is not None and self.selected_button != button:
                        self.selected_button.view.selected = False
                    button.view.selected = True
                    self.selected_button = button
                    return
        elif event.type == pg.MOUSEBUTTONDOWN:
            click_pos = event.pos
            if self.selected_button is not None and self.selected_button.view.rect.collidepoint(click_pos):
                if self.selected_button.view.text.view.text == START:
                    self.main_menu.states_stack.push(SaveSelectionState(self.main_menu, self.game, self.main_menu.buttons['save_selection_state_buttons']))
                elif self.selected_button.view.text.view.text == EXIT:
                    main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == loc.K_s or event.key == loc.K_DOWN:
                if self.selected_button is not None:
                    self.selected_button.view.selected = False
                    current_button_index = self.buttons.index(self.selected_button)
                    self.selected_button = self.buttons[(current_button_index + 1) % len(self.buttons)]
                else:
                    self.selected_button = self.buttons[0]
                self.selected_button.view.selected = True
            elif event.key == loc.K_w or event.key == loc.K_UP:
                if self.selected_button is not None:
                    self.selected_button.view.selected = False
                    current_button_index = self.buttons.index(self.selected_button)
                    self.selected_button = self.buttons[(current_button_index - 1) % len(self.buttons)]
                else:
                    self.selected_button = self.buttons[0]
                self.selected_button.view.selected = True
            elif event.key == loc.K_RETURN:
                if self.selected_button is not None:
                    if self.selected_button.view.text.view.text == START:
                        self.main_menu.states_stack.push(SaveSelectionState(self.main_menu, self.game, self.main_menu.buttons['save_selection_state_buttons']))
                    elif self.selected_button.view.text.view.text == EXIT:
                        main_process.is_running = False

    def draw(self):
        self.main_menu.view.render(self.buttons)
        self.main_menu.view.display.update()


class SaveSelectionState(MainMenuState):
    def __init__(self, main_menu, game, buttons):
        super().__init__(main_menu, game, buttons)
        self.selected_button = None

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.MOUSEMOTION:
            mouse_pos = event.pos
            for button in self.buttons:
                if button.view.rect.collidepoint(mouse_pos):
                    if self.selected_button is not None and self.selected_button != button:
                        self.selected_button.view.selected = False
                    button.view.selected = True
                    self.selected_button = button
                    return
            if self.selected_button is not None:
                self.selected_button.view.selected = False
                self.selected_button = None
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed(3)[0]:
                if self.selected_button is not None:
                    mouse_click_pos = event.pos
                    if self.selected_button.view.rect.collidepoint(mouse_click_pos):
                        if self.selected_button.view.text.view.text == SELECT_1:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_2:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_3:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_4:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_5:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_1_AUTO:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_2_AUTO:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_3_AUTO:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_4_AUTO:
                            pass
                        elif self.selected_button.view.text.view.text == SELECT_5_AUTO:
                            pass



    def draw(self):
        self.main_menu.view.render(self.buttons)
        self.main_menu.view.display.update()