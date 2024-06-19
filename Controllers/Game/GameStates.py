import pygame as pg

from Controllers.Game.BaseStates import GameState
from Controllers.Entity.States.PlayerStates import InventoryOpenState, PlayerStealState
from Controllers.Game.Utils import check_buttons_collisions
from Controllers.Saves.SaveGame import save_game

from Views.Entity.Entity import render_entities
from Views.Entity.HealthBar import render_health_bars

from Utils.DistanceCounting import manhattan_distance
from Utils.Settings.Buttons.Buttons import get_pressed_button
from Utils.Settings.Buttons.ButtonsTexts import *
from Utils.Draw.Text import print_text
from Utils.Settings.Colours import *
from Utils.Settings.Paths import *


class Running(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_f:
                if not self.game.room.live_NPCs_count:
                    for door in self.game.room.collisions_map.doors:
                        if door.get_next_room(self.game.room)[-1]:
                            if door.current_tile.collision.rect.collidepoint(pg.mouse.get_pos()):
                                if manhattan_distance(door.current_tile.collision.rect.center, self.game.player.physic.collision.rect.center) <= min(self.game.player.physic.collision.rect.w, self.game.player.physic.collision.rect.h) * 2:
                                    self.game.room, self.game.player.physic.collision.rect.topleft = door.get_next_room(self.game.room)[:2]
                        else:
                            if door.next_tile.collision.rect.collidepoint(pg.mouse.get_pos()):
                                if manhattan_distance(door.next_tile.collision.rect.center, self.game.player.physic.collision.rect.center) <= min(self.game.player.physic.collision.rect.w, self.game.player.physic.collision.rect.h) * 2:
                                    self.game.room, self.game.player.physic.collision.rect.topleft = door.get_next_room(self.game.room)[:2]
            elif event.key == pg.K_p:
                self.game.states_stack.push(OnPause(self.game))
                self.game.states_stack.peek().handle_input(event, processes_stack, main_process)
                return
            elif event.key == pg.K_e:
                old_len = self.game.player.states_stack.size
                self.game.player.states_stack.peek().handle_input(event, self.game.room)
                if self.game.player.states_stack.size() != old_len:
                    self.game.states_stack.push(OnPause(self.game))
                    self.game.states_stack.peek().handle_input(event, processes_stack, main_process)
                    return
            elif event.key == pg.K_ESCAPE:
                self.game.states_stack.push(EscState(self.game, self.game.buttons['esc_state_buttons']))
                return
        old_len = self.game.player.states_stack.size()
        self.game.player.states_stack.peek().handle_input(event, self.game.room)
        if self.game.player.states_stack.size() != old_len:
            self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self):
        self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)
        for NPC in self.game.room.NPCs:
            NPC.states_stack.peek().update(self.game.room, self.game.player, [*self.game.room.NPCs, self.game.player])

    def draw(self):
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        render_entities(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        render_health_bars(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        self.game.view.display.update()


class OnPause(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.finished = True

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                if type(self.game.player.states_stack.peek()) not in [InventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
            elif event.key == pg.K_e:
                if type(self.game.player.states_stack.peek()) in [InventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
        self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self):
        if self.finished:
            self.game.states_stack.pop()
        else:
            self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)

    def draw(self):
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        self.game.player.states_stack.peek().draw(self.game.entities_surface)
        self.game.view.display.update()


class EscState(GameState):
    def __init__(self, game, buttons):
        super().__init__(game)
        self.buttons = buttons
        self.selected_button = None

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                self.finished = True
        elif event.type == pg.MOUSEMOTION:
            check_buttons_collisions(pg.mouse.get_pos(), self)
        elif event.type == pg.MOUSEBUTTONDOWN:
            selected_button = get_pressed_button(self.buttons, event.pos)
            if selected_button.view.text.view.text == CONTINUE:
                self.finished = True
            elif selected_button.view.text.view.text == SAVE_GAME:
                if not self.game.room.live_NPCs_count:
                    self.game.states_stack.push(SaveSelectionState(self.game, self.game.buttons['save_selection_buttons']))
            elif selected_button.view.text.view.text == EXIT_TO_MAIN_MENU:
                self.selected_button.view.selected = False
                self.selected_button = None
                processes_stack.pop()

    def update(self):
        if self.finished:
            if self.selected_button is not None:
                self.selected_button.view.selected = False
                self.selected_button = None
            self.game.states_stack.pop()

    def draw(self):
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        self.game.player.states_stack.peek().draw(self.game.entities_surface)
        for button in self.game.buttons['esc_state_buttons']:
            button.view.render(self.game.view.display.surface)
        self.game.view.display.update()


class SaveSelectionState(GameState):
    def __init__(self, game, buttons):
        super().__init__(game)
        self.buttons = buttons
        self.selected_button = None

    def handle_input(self, event, processes_stack, main_process):
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.MOUSEMOTION:
            check_buttons_collisions(pg.mouse.get_pos(), self)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed(3)[0]:
                if self.selected_button is not None:
                    if self.selected_button.view.text.view.text == SELECT_1_AUTO:
                        save_game(self.game.auto_saves[0], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves()
                    elif self.selected_button.view.text.view.text == SELECT_2_AUTO:
                        save_game(self.game.auto_saves[1], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves()
                    elif self.selected_button.view.text.view.text == SELECT_3_AUTO:
                        save_game(self.game.auto_saves[2], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves()
                    elif self.selected_button.view.text.view.text == SELECT_4_AUTO:
                        save_game(self.game.auto_saves[3], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves()
                    elif self.selected_button.view.text.view.text == SELECT_5_AUTO:
                        save_game(self.game.auto_saves[4], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves()
                    elif self.selected_button.view.text.view.text == SELECT_1:
                        save_game(self.game.saves[0], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                    elif self.selected_button.view.text.view.text == SELECT_2:
                        save_game(self.game.saves[1], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                    elif self.selected_button.view.text.view.text == SELECT_3:
                        save_game(self.game.saves[2], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                    elif self.selected_button.view.text.view.text == SELECT_4:
                        save_game(self.game.saves[3], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                    elif self.selected_button.view.text.view.text == SELECT_5:
                        save_game(self.game.saves[4], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                    elif self.selected_button.view.text.view.text == CANSEL:
                        self.game.states_stack.pop()

    def update(self):
        if self.finished:
            if self.selected_button is not None:
                self.selected_button.view.selected = False
                self.selected_button = None
            self.game.states_stack.pop()

    def draw(self):
        self.game.view.display.surface.fill(DARK_GRAY_RGB)
        line_start_pos = [135, 20]
        line_end_pos = [135, 200]
        date_start_pos = [0, 50]
        for button in self.buttons:
            button.view.render(self.game.view.display.surface)
        print_text(self.game.view.display.surface, self.game.auto_saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        for auto_save in self.game.auto_saves[1:]:
            pg.draw.line(self.game.view.display.surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
            date_start_pos[0] += 140
            print_text(self.game.view.display.surface, auto_save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
            line_start_pos[0] += 140
            line_end_pos[0] += 140
        line_start_pos = [135, 210]
        line_end_pos = [135, 390]
        date_start_pos = [0, 250]
        print_text(self.game.view.display.surface, self.game.saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        for save in self.game.saves[1:]:
            pg.draw.line(self.game.view.display.surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
            date_start_pos[0] += 140
            print_text(self.game.view.display.surface, save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
            line_start_pos[0] += 140
            line_end_pos[0] += 140
        self.game.view.display.update()