from Controllers.Entity.States.BaseStates import NPCState
from Controllers.Entity.Utils import get_damage_and_movement

from Utils.DistanceCounting import manhattan_distance


def check_damage_for_NPC(entity, damage_map):
    damage, movement = get_damage_and_movement(damage_map, entity.physic.collision.rect)
    if damage:
        entity.states_stack.push(NPCAfterPunchState(entity))
        entity.states_stack.peek().movement = movement
        entity.states_stack.peek().damage = damage
        return True
    return False


class NPCDeathState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)


class NPCAfterPunchState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)
        self.movement = (0, 0)
        self.damage = {}

    def update(self, room, player, entities):
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage
        self.entity.health.health -= damage
        if self.entity.health.health <= 0:
            room.live_NPCs_count -= 1
            self.entity.states_stack.push(NPCDeathState(self.entity))
            return
        self.entity.physic.collision.get_collisions_around(room.collisions_map.map, room.view.tile_size)
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()


class NPCIdleState(NPCState):
    def update(self, room, player, entities):
        if check_damage_for_NPC(self.entity, room.collisions_map.damage_map):
            return
        self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around["center"].rect.x, self.entity.physic.collision.collisions_around["center"].rect.y), (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y), room.collisions_map.graph)
        self.old_player_center_pos = (player.physic.collision.collisions_around["center"].rect.x, player.physic.collision.collisions_around["center"].rect.y)
        self.entity.states_stack.push(NPCWalkState(self.entity))


class NPCWalkState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)

    def update(self, room, player, entities):
        if check_damage_for_NPC(self.entity, room.collisions_map.damage_map):
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
            if entities_around[direction] is not None:
                new_state = NPCPunchState(self.entity)
                new_state.direction_for_punch = direction
                self.entity.states_stack.push(new_state)
                return


class NPCPunchState(NPCState):
    def __init__(self, entity):
        super().__init__(entity)
        self.direction_for_punch = None

    def update(self, room, player, entities):
        if check_damage_for_NPC(self.entity, room.collisions_map.damage_map):
            return
        if self.finished:
            if self.direction_for_punch == 'up':
                self.entity.current_item.set_animation(0, self.entity)
            elif self.direction_for_punch == 'right':
                self.entity.current_item.set_animation(90, self.entity)
            elif self.direction_for_punch == 'down':
                self.entity.current_item.set_animation(180, self.entity)
            else:
                self.entity.current_item.set_animation(270, self.entity)
            if self.entity.current_item.view.copied_animation is not None:
                room.collisions_map.add_damage(self.entity.current_item.physic.attack_physic, id(self.entity.current_item.physic.attack_physic))
                self.finished = False
            else:
                self.finished = True
                self.entity.states_stack.pop()
        elif self.entity.current_item.view.copied_animation.done:
            self.finished = True
            room.collisions_map.remove_damage(id(self.entity.current_item.physic.attack_physic))
            self.entity.states_stack.pop()

    def draw(self):
        self.entity.view.render((self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_item.view.copied_animation.render(self.entity.view.surface)