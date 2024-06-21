from Controllers.Entities.States.AbstractStates import NPCAbstractState


class NPCBaseState(NPCAbstractState):
    def __init__(self, entity):
        self.entity = entity
        self.old_player_center_pos = None
        self.finished = True

    def update(self, room, player, entities):
        pass

    def draw(self, surface):
        self.entity.view.render(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCIdleState(NPCBaseState):
    def update(self, room, player, entities):
        if self.entity.health.health <= 0:
            self.entity.states_stack.push(self.entity.states_types['death_state'](self.entity))
            return
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types['after_punch_state']):
            return
        self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y), room.collisions_map.graph)
        self.old_player_center_pos = (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y)
        self.entity.states_stack.push(SwordsmanWalkState(self.entity))

    def draw(self, surface):
        self.entity.view.render(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCWalkState(NPCBaseState):
    def update(self, room, player, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types['after_punch_state']):
            return
        current_player_center_pos = (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y)
        if current_player_center_pos == self.old_player_center_pos and manhattan_distance((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos) > max(player.physic.collision.rect.width, player.physic.collision.rect.height) * 2:
            if self.entity.mind.way:
                next_coord = self.entity.mind.way[0]
                if self.entity.physic.collision.collisions_around['center'].rect.x < next_coord[0]:
                    self.entity.view.rotate(90)
                    self.entity.physic.velocity[0] = self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.x > next_coord[0]:
                    self.entity.view.rotate(270)
                    self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.y < next_coord[1]:
                    self.entity.view.rotate(180)
                    self.entity.physic.velocity[1] = self.entity.physic.max_velocity
                if self.entity.physic.collision.collisions_around['center'].rect.y > next_coord[1]:
                    self.entity.view.rotate(0)
                    self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
                elif self.entity.physic.collision.collisions_around['center'].rect.y == next_coord[1] and self.entity.physic.collision.collisions_around['center'].rect.x == next_coord[0]:
                    self.entity.mind.way.pop(0)
        elif current_player_center_pos != self.old_player_center_pos and manhattan_distance((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos) > max(player.physic.collision.rect.width, player.physic.collision.rect.height) * 2:
            self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), current_player_center_pos, room.collisions_map.graph)
            self.old_player_center_pos = current_player_center_pos
        else:
            self.entity.states_stack.pop()
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.view.tile_size)
        entities_around = self.entity.physic.collision.update(self.entity.physic.velocity, entities)
        for direction in entities_around:
            if entities_around[direction] == player:
                self.entity.states_stack.push(self.entity.states_types['punch_state'](self.entity, direction))
                return


class NPCAfterPunchState(NPCBaseState):
    def __init__(self, entity, movement, damage):
        super().__init__(entity)
        self.movement = movement
        self.damage = damage

    def update(self, room, player, entities):
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage_types[damage_type]
        self.entity.health.health -= damage
        if self.entity.health.health <= 0:
            room.live_NPCs_count -= 1
            room.loot_tiles.append(LootTile(self.entity.physic.collision.rect.topleft, self.entity.inventory))
            self.entity.states_stack.push(SwordsmanDeathState(self.entity))
            return
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()


class NPCPunchState(NPCBaseState):
    def __init__(self, entity, direction_for_punch):
        super().__init__(entity)
        self.direction_for_punch = direction_for_punch
        self.copied_damage_rect = None

    def update(self, room, player, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, SwordsmanAfterPunchState):
            return
        if self.finished:
            if self.direction_for_punch == 'up':
                direction = 0
            elif self.direction_for_punch == 'right':
                direction = 90
            elif self.direction_for_punch == 'down':
                direction = 180
            else:
                direction = 270
            if self.entity.current_weapon.attack(room, direction, self.entity, self):
                self.finished = False
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif self.entity.current_weapon.view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.copied_damage_rect))
            self.entity.states_stack.pop()

    def draw(self, surface):
        self.entity.view.render(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_weapon.view.copied_animation.render(surface)


class NPCDeathState(NPCBaseState):
    pass
