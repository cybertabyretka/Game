import pygame as pg


class AttackPhysic:
    def __init__(self, attack_size, damage_types):
        self.direction = None
        self.attack_size = attack_size
        self.rect = None
        self.damage_types = damage_types

    def copy(self):
        copied_attack_phy = AttackPhysic(self.attack_size, self.damage_types)
        copied_attack_phy.direction = self.direction
        copied_attack_phy.rect = self.rect
        return copied_attack_phy

    def set_attack_rect(self, start_pos, direction):
        self.rect = pg.Rect(start_pos[0], start_pos[1], self.attack_size[0], self.attack_size[1])
        self.direction = direction


class SwordAttackPhysics(AttackPhysic):
    def __init__(self, attack_size, damage_types):
        super().__init__(attack_size, damage_types)

    def copy(self):
        copied_attack_phy = SwordAttackPhysics(self.attack_size, self.damage_types)
        copied_attack_phy.direction = self.direction
        copied_attack_phy.rect = self.rect
        return copied_attack_phy


class StaffAttackPhysic:
    def __init__(self, projectile):
        self.projectile = projectile

    def set_attack_rect(self, start_pos, direction):
        self.projectile.physic.set_attack_rect(start_pos, direction)

    def copy(self):
        return self.projectile.copy()
