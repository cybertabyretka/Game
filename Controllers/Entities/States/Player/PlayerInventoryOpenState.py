import pygame as pg

from Controllers.GetPressedButton import get_pressed_button
from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.CheckMouseButtons import *
from Controllers.SwitchItems import switch_items

from BaseVariables.Buttons.ButtonsTexts import *


class PlayerInventoryOpenState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.selected_cell = None
        self.buttons = []

    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_e:
                self.finished = not self.finished
                if self.selected_cell is not None:
                    self.selected_cell.change_state()
        elif event.type == pg.MOUSEBUTTONDOWN:
            mouse_click_pos = event.pos
            if check_left_mouse_button():
                if self.buttons:
                    pressed_button = get_pressed_button(self.buttons, mouse_click_pos)
                    if pressed_button is not None:
                        if pressed_button.view.text.view.text == SWITCH_WEAPONS:
                            self.entity.current_weapon = self.entity.change_current_special_item(self.entity.current_weapon, self.selected_cell)
                        elif pressed_button.view.text.view.text == SWITCH_SHIELDS:
                            self.entity.current_shield = self.entity.change_current_special_item(self.entity.current_shield, self.selected_cell)
                        self.selected_cell.change_state()
                        self.selected_cell = None
                    self.buttons = []
                    return
                if self.entity.view.windows['inventory_base'].view.rect.collidepoint(mouse_click_pos):
                    inventory_cell_index = self.entity.inventory.get_cell_index_from_pos(mouse_click_pos, self.entity.view.windows['inventory_base'])
                    if self.entity.inventory.size[0] > inventory_cell_index[0] >= 0 and self.entity.inventory.size[1] > inventory_cell_index[1] >= 0:
                        if self.selected_cell is None:
                            self.selected_cell = self.entity.inventory.get_cell(inventory_cell_index)
                            self.selected_cell.change_state()
                        else:
                            switch_items(self.selected_cell, self.entity.inventory.get_cell(inventory_cell_index))
                            self.selected_cell.change_state()
                            self.selected_cell = None
            elif check_right_mouse_button():
                if self.entity.view.windows['inventory_base'].view.rect.collidepoint(mouse_click_pos):
                    inventory_cell_index = self.entity.inventory.get_cell_index_from_pos(mouse_click_pos, self.entity.view.windows['inventory_base'])
                    if self.entity.inventory.size[0] > inventory_cell_index[0] >= 0 and self.entity.inventory.size[1] > inventory_cell_index[1] >= 0:
                        if self.selected_cell is not None:
                            self.selected_cell.change_state()
                            self.selected_cell = None
                        selected_item = self.entity.inventory.get_cell(inventory_cell_index).item
                        selected_item.set_buttons_start_pos(mouse_click_pos)
                        self.buttons = selected_item.buttons
                        self.selected_cell = self.entity.inventory.get_cell(inventory_cell_index)
                        self.selected_cell.change_state()
        elif event.type == pg.KEYUP and len(self.events) < 35:
            self.events.append(event)

    def draw(self, surface):
        self.entity.view.windows['inventory_base'].view.draw(surface, self.entity.inventory.view, self.entity.inventory.cells)
        for button in self.buttons:
            button.view.draw(surface)