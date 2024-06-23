import pygame as pg

from Controllers.Entities.States.Player.PlayerBaseState import PlayerBaseState
from Controllers.Weapons.AttackPhysic import AttackPhysic

from Models.Entities.BaseEntity import Entity
from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile
from Models.Room.Room import Room


class PlayerAfterPunchState(PlayerBaseState):
    def __init__(self, entity: Entity, movement: list[int, int], damage: dict[str, list[AttackPhysic | BaseProjectile]]):
        super().__init__(entity)
        self.movement: list[int, int] = movement
        self.damage: dict[str, list[AttackPhysic | BaseProjectile]] = damage

    def handle_input(self, event: pg.event, room: Room) -> None:
        if len(self.events) < 35:
            self.events.append(event)

    def update(self, room: Room, entities: list[Entity]) -> None:
        damage = 0
        for damage_type in self.damage:
            for damage_rect in self.damage[damage_type]:
                damage += damage_rect.damage_types[damage_type]
        self.entity.health.health -= damage
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()
        self.entity.states_stack.peek().handle_inputs(self.events, room)