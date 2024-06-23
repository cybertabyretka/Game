from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity

from Constants.StatesNames import *
from Constants.Directions import *

from Models.Entities.BaseEntity import Entity
from Models.Entities.Player import Player
from Models.Room.Room import Room

from Utils.DistanceCounting import manhattan_distance


class NPCWalkState(NPCBaseState):
    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
        current_player_center_pos = (player.physic.collision.collisions_around[CENTER].rect.x, player.physic.collision.collisions_around[CENTER].rect.y)
        if manhattan_distance((self.entity.physic.collision.collisions_around[CENTER].rect.x, self.entity.physic.collision.collisions_around[CENTER].rect.y), current_player_center_pos) > max(player.physic.collision.rect.w, player.physic.collision.rect.h) * 2:
            if current_player_center_pos == self.old_player_center_pos:
                if self.entity.mind.way:
                    next_coord = self.entity.mind.way[0]
                    if self.entity.physic.collision.collisions_around[CENTER].rect.x < next_coord[0]:
                        self.entity.view.rotate(90)
                        self.entity.physic.velocity[0] = self.entity.physic.max_velocity
                    if self.entity.physic.collision.collisions_around[CENTER].rect.x > next_coord[0]:
                        self.entity.view.rotate(270)
                        self.entity.physic.velocity[0] = -self.entity.physic.max_velocity
                    if self.entity.physic.collision.collisions_around[CENTER].rect.y < next_coord[1]:
                        self.entity.view.rotate(180)
                        self.entity.physic.velocity[1] = self.entity.physic.max_velocity
                    if self.entity.physic.collision.collisions_around[CENTER].rect.y > next_coord[1]:
                        self.entity.view.rotate(0)
                        self.entity.physic.velocity[1] = -self.entity.physic.max_velocity
                    elif self.entity.physic.collision.collisions_around[CENTER].rect.y == next_coord[1] and self.entity.physic.collision.collisions_around[CENTER].rect.x == next_coord[0]:
                        self.entity.mind.way.pop(0)
            else:
                self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around[CENTER].rect.x, self.entity.physic.collision.collisions_around[CENTER].rect.y), current_player_center_pos, room.collisions_map.graph)
                self.old_player_center_pos = current_player_center_pos
        else:
            self.entity.states_stack.pop()
        entities_around = self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map)
        for direction in entities_around:
            if entities_around[direction] == player:
                self.entity.states_stack.push(self.entity.states_types[PUNCH_STATE](self.entity, direction))
                return