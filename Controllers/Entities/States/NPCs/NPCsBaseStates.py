import pygame as pg

from Models.Room.Tile import LootTile

from Controllers.Entities.States.AbstractStates import NPCAbstractState
from Controllers.Entities.Physic.DamageProcess import check_damage_for_entity
from Controllers.Weapons.AttackPhysic import AttackPhysic

from Constants.Directions import *

from Models.Entities.BaseEntity import Entity
from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile
from Models.Room.Room import Room
from Models.Entities.Player import Player

from Utils.DistanceCounting import manhattan_distance


class NPCBaseState(NPCAbstractState):
    def __init__(self, entity: Entity):
        self.entity: Entity = entity
        self.old_player_center_pos: tuple[int, int] | None = None
        self.finished: bool = True

    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        pass

    def draw(self, surface: pg.Surface) -> None:
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCIdleState(NPCBaseState):
    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        if self.entity.health.health <= 0:
            self.entity.states_stack.push(self.entity.states_types['death_state'](self.entity))
            return
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types['after_punch_state']):
            return
        self.entity.mind.search_way_in_graph((self.entity.physic.collision.collisions_around[CENTER].rect.x, self.entity.physic.collision.collisions_around[CENTER].rect.y), (player.physic.collision.collisions_around[CENTER].rect.x, player.physic.collision.collisions_around[CENTER].rect.y), room.collisions_map.graph)
        self.old_player_center_pos = (player.physic.collision.collisions_around[CENTER].rect.x, player.physic.collision.collisions_around[CENTER].rect.y)
        self.entity.states_stack.push(self.entity.states_types['walk_state'](self.entity))

    def draw(self, surface: pg.Surface) -> None:
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))


class NPCWalkState(NPCBaseState):
    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types['after_punch_state']):
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
                self.entity.states_stack.push(self.entity.states_types['punch_state'](self.entity, direction))
                return


class NPCAfterPunchState(NPCBaseState):
    def __init__(self, entity: Entity, movement: list[int], damage: dict[str, list[AttackPhysic | BaseProjectile]]):
        super().__init__(entity)
        self.movement: list[int] = movement
        self.damage: dict[str, list[AttackPhysic | BaseProjectile]] = damage

    def update(self, room: Room, player: Player, entities: list[Entity]) -> None:
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage_types[damage_type]
        self.entity.health.health -= damage
        if self.entity.health.health <= 0:
            room.live_NPCs_count -= 1
            room.loot_tiles.append(LootTile(self.entity.physic.collision.rect.topleft, self.entity.inventory))
            self.entity.states_stack.push(self.entity.states_types['death_state'](self.entity))
            return
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()


class NPCPunchState(NPCBaseState):
    def __init__(self, entity: Entity, direction_for_punch: str):
        super().__init__(entity)
        self.direction_for_punch: str = direction_for_punch
        self.copied_damage_rect: AttackPhysic | None = None

    def update(self, room, player, entities):
        if check_damage_for_entity(self.entity, room.collisions_map.damage_map, room.collisions_map.movable_damage_map, self.entity.states_types['after_punch_state']):
            return
        if self.finished:
            if self.direction_for_punch == UP:
                direction = 0
            elif self.direction_for_punch == RIGHT:
                direction = 90
            elif self.direction_for_punch == DOWN:
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
        self.entity.view.draw(surface, (self.entity.physic.collision.rect.x, self.entity.physic.collision.rect.y))
        if not self.finished:
            self.entity.current_weapon.view.copied_animation.draw(surface)


class NPCDeathState(NPCBaseState):
    pass
