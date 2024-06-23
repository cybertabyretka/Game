import pygame as pg

from BaseVariables.Buttons.ButtonsTexts import *
from BaseVariables.Entities.PlayerStatesTypes import *

from Constants.Colours import *
from Constants.StatesNames import *

from DataStructures.Stack import Stack

from Controllers.Game.States.BaseStates import GameState
from Controllers.Game.States.ButtonsCheck import check_buttons_collisions
from Controllers.Saves.SaveGame import save_game
from Controllers.Game.Processes.MainProcess import MainProcess

from Controllers.GetPressedButton import get_pressed_button
from Models.Items.Item import EmptyItem

from Utils.DistanceCounting import manhattan_distance

from Views.Entities.DrawEntities import draw_entities
from Views.HealthBars.DrawHealthBars import draw_health_bars
from Views.Items.Projectiles.DrawProjectiles import draw_projectiles
from Views.AppStates.DrawSaveSelectionState import draw_save_selection_state

from Models.InteractionObjects.Button import Button


class Running(GameState):
    def __init__(self, game):
        super().__init__(game)

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
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

    def update(self) -> None:
        self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)
        for NPC in self.game.room.NPCs:
            NPC.states_stack.peek().update(self.game.room, self.game.player, [*self.game.room.NPCs, self.game.player])
        i = 0
        while i < len(self.game.room.collisions_map.movable_damage_map):
            current_projectile = self.game.room.collisions_map.movable_damage_map[i]
            current_projectile.physic.collision.update(current_projectile.physic.velocity, self.game.room, i)
            i += 1

    def draw(self) -> None:
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        draw_entities(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        draw_health_bars(self.game.room.NPCs, self.game.player, self.game.entities_surface)
        draw_projectiles(self.game.room.collisions_map.movable_damage_map, self.game.entities_surface)
        self.game.view.display.update()


class OnPause(GameState):
    def __init__(self, game):
        super().__init__(game)
        self.finished: bool = True

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_p:
                if type(self.game.player.states_stack.peek()) not in [PlayerInventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
            elif event.key == pg.K_e:
                if type(self.game.player.states_stack.peek()) in [PlayerInventoryOpenState, PlayerStealState]:
                    self.finished = not self.finished
        self.game.player.states_stack.peek().handle_input(event, self.game.room)

    def update(self) -> None:
        if self.finished:
            self.game.states_stack.pop()
        else:
            self.game.player.states_stack.peek().update(self.game.room, self.game.room.NPCs)

    def draw(self) -> None:
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        self.game.player.states_stack.peek().draw(self.game.entities_surface)
        self.game.view.display.update()


class EscState(GameState):
    def __init__(self, game, buttons: list[Button]):
        super().__init__(game)
        self.buttons: list[Button] = buttons
        self.selected_button: Button | None = None

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
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

    def update(self) -> None:
        if self.finished:
            if self.selected_button is not None:
                self.selected_button.view.selected = False
                self.selected_button = None
            self.game.states_stack.pop()

    def draw(self) -> None:
        self.game.room.view.render_tile_map(self.game.rooms_surface)
        self.game.rooms_surface.blit(self.game.entities_surface, (0., 0.))
        self.game.view.display.surface.blit(self.game.rooms_surface, (self.game.rooms_surface.get_rect().x, self.game.rooms_surface.get_rect().y))
        self.game.player.states_stack.peek().draw(self.game.entities_surface)
        for button in self.game.buttons['esc_state_buttons']:
            button.view.draw(self.game.view.display.surface)
        self.game.view.display.update()


class SaveSelectionState(GameState):
    def __init__(self, game, buttons: list[Button]):
        super().__init__(game)
        self.buttons: list[Button] = buttons
        self.selected_button: Button | None = None

    def handle_input(self, event: pg.event, processes_stack: Stack, main_process: MainProcess) -> None:
        if event.type == pg.QUIT:
            main_process.is_running = False
        elif event.type == pg.MOUSEMOTION:
            check_buttons_collisions(pg.mouse.get_pos(), self)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if pg.mouse.get_pressed(3)[0]:
                if self.selected_button is not None:
                    if self.selected_button.view.text.view.text == SELECT_1_AUTO:
                        save_game(self.game.auto_saves[0], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves_indexes()
                    elif self.selected_button.view.text.view.text == SELECT_2_AUTO:
                        save_game(self.game.auto_saves[1], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves_indexes()
                    elif self.selected_button.view.text.view.text == SELECT_3_AUTO:
                        save_game(self.game.auto_saves[2], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves_indexes()
                    elif self.selected_button.view.text.view.text == SELECT_4_AUTO:
                        save_game(self.game.auto_saves[3], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves_indexes()
                    elif self.selected_button.view.text.view.text == SELECT_5_AUTO:
                        save_game(self.game.auto_saves[4], self.game.view.rooms_map.copy_for_save(self.game.room), self.game.player.copy_for_save())
                        self.game.sort_auto_saves_indexes()
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
                    EmptyItem().view.download_images()

    def update(self) -> None:
        if self.finished:
            if self.selected_button is not None:
                self.selected_button.view.selected = False
                self.selected_button = None
            self.game.states_stack.pop()

    def draw(self) -> None:
        draw_save_selection_state(self.game.view.display.surface, self.buttons, self.game.auto_saves, self.game.saves, DARK_GRAY_RGB)
        self.game.view.display.update()