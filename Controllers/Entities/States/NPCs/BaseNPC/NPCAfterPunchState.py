from Controllers.Entities.States.NPCs.BaseNPC.NPCsBaseState import NPCBaseState
from Controllers.Weapons.AttackPhysic import AttackPhysic

from Constants.StatesNames import *

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile
from Models.Room.Room import Room
from Models.Entities.BaseEntity import Entity
from Models.Entities.Player import Player
from Models.Room.Tile import LootTile


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
            self.entity.states_stack.push(self.entity.states_types[DEATH_STATE](self.entity))
            return
        self.entity.physic.collision.update(self.entity.physic.velocity, entities, room.collisions_map.map, movement=self.movement)
        self.finished = True
        self.entity.states_stack.pop()