import pygame as pg

from Controllers.Weapons.AttackPhysic import AttackPhysic

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile
from Models.Entities.BaseEntity import Entity


def get_damage_and_movement(damage_map: dict[str, AttackPhysic], movable_damage_map: list[BaseProjectile], entity_rect: pg.Rect) -> tuple[dict[str, list[AttackPhysic | BaseProjectile]], tuple[int, int]]:
    types: dict[str, list[AttackPhysic | BaseProjectile]] = {}
    movement: tuple[int, int] = (0, 0)
    for identifier in damage_map:
        damage_rect = damage_map[identifier]
        if entity_rect.colliderect(damage_rect.rect):
            for damage_type in damage_rect.damage_types:
                if damage_type not in types:
                    types[damage_type] = [damage_rect.copy()]
                else:
                    types[damage_type].append(damage_rect.copy())
                if damage_rect.direction == 0:
                    movement = (0, -entity_rect.width // 2)
                elif damage_rect.direction == 90:
                    movement = (entity_rect.width // 2, 0)
                elif damage_rect.direction == 180:
                    movement = (0, entity_rect.width // 2)
                else:
                    movement = (-entity_rect.width // 2, 0)
    indexes_to_del: list[int] = []
    for i in range(len(movable_damage_map)):
        if entity_rect.colliderect(movable_damage_map[i].physic.collision.rect):
            indexes_to_del.append(i)
            for damage_type in movable_damage_map[i].physic.damage_types:
                if damage_type not in types:
                    types[damage_type] = [movable_damage_map[i].physic.copy()]
                else:
                    types[damage_type].append(movable_damage_map[i].physic.copy())
                if movable_damage_map[i].physic.direction == 0:
                    movement = (0, -entity_rect.width // 2)
                elif movable_damage_map[i].physic.direction == 90:
                    movement = (entity_rect.width // 2, 0)
                elif movable_damage_map[i].physic.direction == 180:
                    movement = (0, entity_rect.width // 2)
                else:
                    movement = (-entity_rect.width // 2, 0)
    for i in range(len(indexes_to_del)-1, -1, -1):
        del movable_damage_map[indexes_to_del[i]]
    return types, movement


def check_damage_for_entity(entity: Entity, damage_map: dict[str, AttackPhysic], movable_damage_map: list[BaseProjectile], after_punch_state) -> bool:
    damage, movement = get_damage_and_movement(damage_map, movable_damage_map, entity.physic.collision.rect)
    if damage:
        entity.states_stack.push(after_punch_state(entity, movement, damage))
        return True
    return False


def check_damage_for_entity_with_ready_damage_and_movement(entity: Entity, damage: dict[str, list[AttackPhysic | BaseProjectile]], movement: tuple[int, int], after_punch_state) -> bool:
    if damage:
        entity.states_stack.push(after_punch_state(entity, movement, damage))
        return True
    return False
