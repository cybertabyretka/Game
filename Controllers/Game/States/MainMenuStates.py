import pygame as pg
import pygame.locals as loc

from BaseVariables.Buttons.ButtonsTexts import *
from BaseVariables.Game import BASE_ROOMS_MAP, BASE_PLAYER

from DataStructures.Stack import Stack

from Constants.Colours import DARK_GRAY_RGB

from Controllers.Game.States.BaseStates import MainMenuState
from Controllers.Game.States.ButtonsCheck import check_buttons_collisions
from Controllers.Saves.GetGame import get_game
from Controllers.CheckMouseButtons import check_left_mouse_button
from Controllers.Game.Processes.MainProcess import MainProcess

from Models.AppStates.Game import Game

from Views.AppStates.DrawSaveSelectionState import draw_save_selection_state

from Models.InteractionObjects.Button import Button


class StartState(MainMenuState):
    def __init__(self, main_menu, buttons: list[Button]):
        super().__init__(main_menu, buttons)
        self.selected_button: Button | None = None

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
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

    def draw(self) -> None:
        self.main_menu.view.draw(self.buttons)
        self.main_menu.view.display.update()


class SaveSelectionState(MainMenuState):
    def __init__(self, main_menu, buttons: list[Button]):
        super().__init__(main_menu, buttons)
        self.selected_button: Button | None = None

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.MOUSEMOTION:
            check_buttons_collisions(pg.mouse.get_pos(), self)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_left_mouse_button():
                if self.selected_button is not None:
                    mouse_click_pos = event.pos
                    if self.selected_button.view.rect.collidepoint(mouse_click_pos):
                        game = None
                        if self.selected_button.view.text.view.text == SELECT_1:
                            game = get_game(self.main_menu.saves[0], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_2:
                            game = get_game(self.main_menu.saves[1], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_3:
                            game = get_game(self.main_menu.saves[2], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_4:
                            game = get_game(self.main_menu.saves[3], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_5:
                            game = get_game(self.main_menu.saves[5], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_1_AUTO:
                            game = get_game(self.main_menu.auto_saves[0], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_2_AUTO:
                            game = get_game(self.main_menu.auto_saves[1], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_3_AUTO:
                            game = get_game(self.main_menu.auto_saves[2], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_4_AUTO:
                            game = get_game(self.main_menu.auto_saves[3], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == SELECT_5_AUTO:
                            game = get_game(self.main_menu.auto_saves[4], self.main_menu.view.display, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                        elif self.selected_button.view.text.view.text == NEW_GAME:
                            game = Game(self.main_menu.view.display, BASE_ROOMS_MAP, BASE_PLAYER, self.main_menu.entities_surface, self.main_menu.rooms_surface, self.main_menu.auto_saves, self.main_menu.saves)
                            game.after_load_preprocess()
                        elif self.selected_button.view.text.view.text == CANSEL:
                            if self.selected_button is not None:
                                self.selected_button.view.selected = False
                            self.main_menu.states_stack.pop()
                        if game is not None:
                            if self.selected_button is not None:
                                self.selected_button.view.selected = False
                                self.selected_button = None
                            processes_stack.push(game)

    def draw(self) -> None:
        draw_save_selection_state(self.main_menu.view.display.surface, self.buttons, self.main_menu.auto_saves, self.main_menu.saves, DARK_GRAY_RGB)
        self.main_menu.view.display.update()
