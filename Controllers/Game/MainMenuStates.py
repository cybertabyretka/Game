import sys

import pygame as pg
import pygame.locals as loc

from Controllers.Game.BaseStates import MainMenuState
from Controllers.Save import get_game

from Models.Game.Game import Game

from Utils.Settings.Buttons.ButtonsTexts import *
from Utils.Draw.Text import print_text
from Utils.Settings.Colours import WHITE_RGB
from Utils.Settings.Paths import FONT_PATH
from Utils.Settings.Saves.Saves import *
from Utils.BaseGame import BASE_ROOMS_MAP, BASE_PLAYER


class StartState(MainMenuState):
    def __init__(self, main_menu, buttons):
        super().__init__(main_menu, buttons)
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
                    if self.selected_button is not None:
                        self.selected_button.view.selected = False
                    self.main_menu.states_stack.push(SaveSelectionState(self.main_menu, self.main_menu.buttons['save_selection_state_buttons']))
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
                        if self.selected_button is not None:
                            self.selected_button.view.selected = False
                        self.main_menu.states_stack.push(SaveSelectionState(self.main_menu, self.main_menu.buttons['save_selection_state_buttons']))
                    elif self.selected_button.view.text.view.text == EXIT:
                        main_process.is_running = False

    def draw(self):
        self.main_menu.view.render(self.buttons)
        self.main_menu.view.display.update()


class SaveSelectionState(MainMenuState):
    def __init__(self, main_menu, buttons):
        super().__init__(main_menu, buttons)
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
                        game = None
                        if self.selected_button.view.text.view.text == SELECT_1:
                            game = get_game(self.main_menu.saves[0], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_2:
                            game = get_game(self.main_menu.saves[1], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_3:
                            game = get_game(self.main_menu.saves[2], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_4:
                            game = get_game(self.main_menu.saves[3], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_5:
                            game = get_game(self.main_menu.saves[5], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_1_AUTO:
                            game = get_game(self.main_menu.auto_saves[0], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_2_AUTO:
                            game = get_game(self.main_menu.auto_saves[1], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_3_AUTO:
                            game = get_game(self.main_menu.auto_saves[2], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_4_AUTO:
                            game = get_game(self.main_menu.auto_saves[3], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == SELECT_5_AUTO:
                            game = get_game(self.main_menu.auto_saves[4], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == NEW_GAME:
                            game = Game(self.main_menu.view.display, BASE_ROOMS_MAP, BASE_PLAYER, self.main_menu.entities_surface, self.main_menu.rooms_surface)
                        elif self.selected_button.view.text.view.text == CANSEL:
                            if self.selected_button is not None:
                                self.selected_button.view.selected = False
                            self.main_menu.states_stack.pop()
                        if game is not None:
                            if self.selected_button is not None:
                                self.selected_button.view.selected = False
                                self.selected_button = None
                            game.download_images()
                            processes_stack.push(game)

    def draw(self):
        line_start_pos = [135, 20]
        line_end_pos = [135, 200]
        date_start_pos = [20, 50]
        self.main_menu.view.render(self.buttons)
        print_text(self.main_menu.view.display.surface, self.main_menu.auto_saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        for auto_save in self.main_menu.auto_saves[1:]:
            pg.draw.line(self.main_menu.view.display.surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
            date_start_pos[0] += 140
            print_text(self.main_menu.view.display.surface, auto_save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
            line_start_pos[0] += 140
            line_end_pos[0] += 140
        line_start_pos = [135, 210]
        line_end_pos = [135, 390]
        date_start_pos = [20, 250]
        print_text(self.main_menu.view.display.surface, self.main_menu.auto_saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        for save in self.main_menu.saves[1:]:
            pg.draw.line(self.main_menu.view.display.surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
            date_start_pos[0] += 140
            print_text(self.main_menu.view.display.surface, save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
            line_start_pos[0] += 140
            line_end_pos[0] += 140
        self.main_menu.view.display.update()