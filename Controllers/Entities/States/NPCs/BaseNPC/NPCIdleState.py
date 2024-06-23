import pygame as pg

from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity

from Constants.Directions import *
from Constants.StatesNames import *

from Models.Entities.BaseEntity import Entity
from Models.Entities.Player import Player
from Models.Room.Room import Room


class NPCIdleState(NPCBaseState):
    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        if self.entity.health.health <= 0:
            self.entity.states_stack.push(self.entity.states_types[DEATH_STATE](self.entity))
            return
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types[AFTER_PUNCH_STATE]):
            return
        self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around[CENTER].rect.x, self.entity.physic.collision.collisions_around[CENTER].rect.y), (player.physic.collision.collisions_around[CENTER].rect.x, player.physic.collision.collisions_around[CENTER].rect.y), room.collisions_map.graph)
        self.old_player_center_pos = (player.physic.collision.collisions_around[CENTER].rect.x, player.physic.collision.collisions_around[CENTER].rect.y)
        self.entity.states_stack.push(self.entity.states_types[WALK_STATE](self.entity))

    def draw(self, surface: pg.Surface) -> None:
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))