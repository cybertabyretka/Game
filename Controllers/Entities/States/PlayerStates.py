from Utils.DistanceCounting import manhattan_distance

from Controllers.GetPressedButton import get_pressed_button
from Models.Inventory.SwitchItems import switch_items

from BaseVariables.Buttons.ButtonsTexts import SWITCH_SHIELDS, SWITCH_WEAPONS

from Constants.Colours import GRAY_RGB

from Controllers.CheckMouseButtons import *
from Controllers.Entities.States.AbstractStates import PlayerAbstractState
from Controllers.Entities.Physic.DamageProcess import *


class PlayerBaseState(PlayerAbstractState):
    def __init__(self, entity):
        self.entity = entity
        self.finished = True
        self.events = []

    def handle_input(self, event, room):
        pass

    def handle_inputs(self, events, room):
        for event in events:
            old_len = self.entity.states_stack.size
            self.handle_input(event, room)
            if self.entity.states_stack.size != old_len:
                self.handle_input(event, room)

    def update(self, room, entities):
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, surface):
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class PlayerIdleState(PlayerBaseState):
    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key in (pg.K_w, pg.K_s, pg.K_a, pg.K_d):
                self.entity.states_stack.push(PlayerWalkState(self.entity))
            elif event.key == pg.K_e:
                if not room.live_NPCs_count:
                    mouse_pos = pg.mouse.get_pos()
                    for steal_tile in room.loot_tiles:
                        if steal_tile.collision.rect.collidepoint(mouse_pos) and manhattan_distance(steal_tile.collision.rect.topleft, self.entity.physic.collision.rect.topleft) <= min(self.entity.physic.collision.rect.w, self.entity.physic.collision.rect.h) * 2:
                            self.entity.states_stack.push(PlayerStealState(self.entity, steal_tile.inventory))
                            return
                    self.entity.states_stack.push(PlayerInventoryOpenState(self.entity))
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_left_mouse_button():
                self.entity.states_stack.push(PlayerPunchState(self.entity))
            elif check_right_mouse_button():
                self.entity.states_stack.push(PlayerShieldState(self.entity))

    def update(self, room, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, PlayerAfterPunchState):
            return


class PlayerWalkState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.directions = set()

    def handle_input(self, event, room):
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_w:
                self.directions.add(pg.K_w)
            elif event.key == pg.K_s:
                self.directions.add(pg.K_s)
            elif event.key == pg.K_a:
                self.directions.add(pg.K_a)
            elif event.key == pg.K_d:
                self.directions.add(pg.K_d)
            elif event.key == pg.K_e:
                if not room.live_NPCs_count:
                    mouse_pos = pg.mouse.get_pos()
                    for steal_tile in room.loot_tiles:
                        if steal_tile.collision.rect.collidepoint(mouse_pos):
                            self.entity.states_stack.push(PlayerStealState(self.entity, steal_tile.inventory))
                            return
                self.entity.states_stack.push(PlayerInventoryOpenState(self.entity))
        elif event.type == pg.KEYUP:
            if event.key == pg.K_w:
                self.entity.physic.velocity[1] = 0
                if pg.K_w in self.directions:
                    self.directions.remove(pg.K_w)
            elif event.key == pg.K_s:
                self.entity.physic.velocity[1] = 0
                if pg.K_s in self.directions:
                    self.directions.remove(pg.K_s)
            elif event.key == pg.K_a:
                self.entity.physic.velocity[0] = 0
                if pg.K_a in self.directions:
                    self.directions.remove(pg.K_a)
            elif event.key == pg.K_d:
                self.entity.physic.velocity[0] = 0
                if pg.K_d in self.directions:
                    self.directions.remove(pg.K_d)
        elif event.type == pg.MOUSEBUTTONDOWN:
            if check_left_mouse_button():
                self.entity.states_stack.push(PlayerPunchState(self.entity))
            elif check_right_mouse_button():
                self.entity.states_stack.push(PlayerShieldState(self.entity))

    def update(self, room, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, PlayerAfterPunchState):
            return
        if len(self.directions) == 0:
            self.entity.states_stack.pop()
            return
        for direction in self.directions:
            if direction == pg.K_w:
                self.entity.view.rotate(0)
                self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
            elif direction == pg.K_s:
                self.entity.view.rotate(180)
                self.entity.physic.velocity[1] = self.entity.physic.max_velocity
            elif direction == pg.K_a:
                self.entity.view.rotate(270)
                self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
            elif direction == pg.K_d:
                self.entity.view.rotate(90)
                self.entity.physic.velocity[0] = self.entity.physic.max_velocity
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map)


class PlayerAfterPunchState(PlayerBaseState):
    def __init__(self, entity, movement, damage):
        super().__init__(entity)
        self.movement = movement
        self.damage = damage

    def handle_input(self, event, room):
        if len(self.events) < 35:
            self.events.append(event)

    def update(self, room, entities):
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage_types[damage_type]
        self.entity.health.health -= damage
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()
        self.entity.states_stack.peek().handle_inputs(self.events, room)


class PlayerPunchState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.copied_damage_rect = None

    def handle_input(self, event, room):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, PlayerAfterPunchState):
            return
        if self.finished:
            self.events = []
            if event.type == pg.MOUSEBUTTONDOWN and check_left_mouse_button():
                direction = -1
                if event.pos[1] < self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 0
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] > self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 90
                elif event.pos[1] > self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 180
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    direction = 270
                if self.entity.current_weapon.attack(room, direction, self.entity, self):
                    self.finished = False
                else:
                    self.finished = True
                    self.entity.states_stack.pop()
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif (event.type == pg.KEYUP or event.type == pg.KEYDOWN) and len(self.events) < 35:
            self.events.append(event)

    def update(self, room, entities):
        if self.entity.current_weapon.view.copied_animation is not None:
            if self.entity.current_weapon.view.copied_animation.done:
                self.finished = True
                room.collisions_map.remove_damage(id(self.copied_damage_rect))
                self.entity.states_stack.pop()
                self.entity.states_stack.peek().handle_inputs(self.events, room)
        else:
            self.finished = True
            room.collisions_map.remove_damage(id(self.copied_damage_rect))
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)

    def draw(self, surface):
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_weapon.view.copied_animation.draw(surface)


class PlayerShieldState(PlayerBaseState):
    def __init__(self, entity):
        super().__init__(entity)
        self.direction = None

    def handle_input(self, event, room):
        if self.finished:
            if event.type == pg.MOUSEBUTTONDOWN and check_right_mouse_button():
                if event.pos[1] < self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 0
                    self.finished = False
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] > self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 90
                    self.finished = False
                elif event.pos[1] > self.entity.physic.collision.rect.y and self.entity.physic.collision.rect.x < event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 180
                    self.finished = False
                elif self.entity.physic.collision.rect.y < event.pos[1] < self.entity.physic.collision.rect.y + self.entity.physic.collision.rect.height and event.pos[0] < self.entity.physic.collision.rect.x + self.entity.physic.collision.rect.width:
                    self.direction = 270
                    self.finished = False
        else:
            if event.type == pg.MOUSEBUTTONUP and not check_right_mouse_button():
                self.finished = True
                self.entity.states_stack.pop()
                self.entity.states_stack.peek().handle_inputs(self.events, room)
            elif event.type == pg.KEYUP or event.type == pg.KEYDOWN:
                self.events.append(event)

    def update(self, room, entities):
        if self.finished:
            self.entity.states_stack.pop()
            self.entity.states_stack.peek().handle_inputs(self.events, room)
        else:
            damage, movement = get_damage_and_movement(room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.physic.collision.rect)
            for damage_type in damage:
                if damage_type in self.entity.current_shield.damage_types:
                    for damage_rect in damage[damage_type]:
                        if damage_rect.direction == 0 and self.direction == 180:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 90 and self.direction == 270:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 180 and self.direction == 0:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
                        elif damage_rect.direction == 270 and self.direction == 90:
                            damage_rect.damage_types[damage_type] = max(0, damage_rect.damage_types[damage_type] - self.entity.current_shield.damage_types[damage_type])
            check_damage_for_entity_with_ready_damage_and_movement(self.entity, damage, movement, PlayerAfterPunchState)

    def draw(self, surface):
        if self.direction == 0:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y-2, self.entity.physic.collision.rect.width, 2))
        elif self.direction == 90:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x+self.entity.physic.collision.rect.width, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        elif self.direction == 180:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y+self.entity.physic.collision.rect.height, self.entity.physic.collision.rect.width, 2))
        else:
            pg.draw.rect(surface, GRAY_RGB, (self.entity.physic.collision.rect.x-2, self.entity.physic.collision.rect.y, 2, self.entity.physic.collision.rect.height))
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


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


class PlayerStealState(PlayerBaseState):
    def __init__(self, entity, inventory_for_steal):
        super().__init__(entity)
        self.inventory_for_steal = inventory_for_steal
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
                elif self.entity.view.windows['inventory_for_steal'].view.rect.collidepoint(mouse_click_pos):
                    inventory_cell_index = self.inventory_for_steal.get_cell_index_from_pos(mouse_click_pos, self.entity.view.windows['inventory_for_steal'])
                    if self.inventory_for_steal.size[0] > inventory_cell_index[0] >= 0 and self.inventory_for_steal.size[1] > inventory_cell_index[1] >= 0:
                        if self.selected_cell is None:
                            self.selected_cell = self.inventory_for_steal.get_cell(inventory_cell_index)
                            self.selected_cell.change_state()
                        else:
                            switch_items(self.selected_cell, self.inventory_for_steal.get_cell(inventory_cell_index))
                            self.selected_cell.change_state()
                            self.selected_cell = None
            elif check_right_mouse_button():
                if self.selected_cell is not None:
                    self.selected_cell.change_state()
                    self.selected_cell = None
                if self.entity.view.windows['inventory_base'].view.rect.collidepoint(mouse_click_pos):
                    inventory_cell_index = self.entity.inventory.get_cell_index_from_pos(mouse_click_pos, self.entity.view.windows['inventory_base'])
                    if self.entity.inventory.size[0] > inventory_cell_index[0] >= 0 and self.entity.inventory.size[1] > inventory_cell_index[1] >= 0:
                        selected_item = self.entity.inventory.get_cell(inventory_cell_index).item
                        selected_item.set_buttons_start_pos(mouse_click_pos)
                        self.buttons = selected_item.buttons
                        self.selected_cell = self.entity.inventory.get_cell(inventory_cell_index)
                        self.selected_cell.change_state()
                elif self.entity.view.windows['inventory_for_steal'].view.rect.collidepoint(mouse_click_pos):
                    inventory_cell_index = self.inventory_for_steal.get_cell_index_from_pos(mouse_click_pos, self.entity.view.windows['inventory_for_steal'])
                    if self.inventory_for_steal.size[0] > inventory_cell_index[0] >= 0 and self.inventory_for_steal.size[1] > inventory_cell_index[1] >= 0:
                        selected_item = self.inventory_for_steal.get_cell(inventory_cell_index).item
                        selected_item.set_buttons_start_pos(mouse_click_pos)
                        self.buttons = selected_item.buttons
                        self.selected_cell = self.inventory_for_steal.get_cell(inventory_cell_index)
                        self.selected_cell.change_state()
        elif event.type == pg.KEYUP and len(self.events) < 35:
            self.events.append(event)

    def draw(self, surface):
        self.entity.view.windows['inventory_base'].view.draw(surface, self.entity.inventory.view, self.entity.inventory.cells)
        self.entity.view.windows['inventory_for_steal'].view.draw(surface, self.inventory_for_steal.view, self.inventory_for_steal.cells)
        for button in self.buttons:
            button.view.draw(surface)