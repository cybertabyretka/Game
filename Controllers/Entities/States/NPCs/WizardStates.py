import time

from Controllers.Entities.States.NPCs.NPCsBaseStates import *


class WizardIdleState(NPCIdleState):
    pass


class WizardWalkState(NPCWalkState):
    def update(self, room, player, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, WizardAfterPunchState):
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
                if time.time() - self.entity.time_since_previous_attack > self.entity.break_time:
                    self.entity.states_stack.push(WizardPunchState(self.entity, direction))
                    self.entity.time_since_previous_attack = time.time()
                return


class WizardAfterPunchState(NPCAfterPunchState):
    pass


class WizardPunchState(NPCPunchState):
    pass


class WizardDeathState(NPCDeathState):
    pass