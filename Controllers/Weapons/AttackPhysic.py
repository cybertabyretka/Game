import pygame as pg

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile


class AttackPhysic:
    def __init__(self, attack_size: tuple[int, int], damage_types: dict[str, int]):
        self.direction: int | None = None
        self.attack_size: tuple[int, int] = attack_size
        self.rect: pg.Rect | None = None
        self.damage_types: dict[str, int] = damage_types

    def copy(self):
        return AttackPhysic(self.attack_size, self.damage_types)

    def set_attack_rect(self, start_pos: tuple[int, int], direction: int) -> None:
        self.rect = pg.Rect(start_pos, self.attack_size)
        self.direction = direction


class SwordAttackPhysics(AttackPhysic):
    def copy(self):
        return SwordAttackPhysics(self.attack_size, self.damage_types)


class StaffAttackPhysic:
    def __init__(self, projectile: BaseProjectile):
        self.projectile: BaseProjectile = projectile

    def set_attack_rect(self, start_pos: tuple[int, int], direction: int) -> None:
        self.projectile.physic.set_attack_rect(start_pos, direction)

    def copy(self):
        return self.projectile.copy()
