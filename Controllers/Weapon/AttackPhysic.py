import pygame as pg


class SwordLikeAttackPhysics:
    def __init__(self, attack_size):
        self.direction = None
        self.attack_size = attack_size
        self.rect = None
        self.type = 'sword'
        self.damage = 1

    def copy(self):
        copied_attack_phy = SwordLikeAttackPhysics(self.attack_size)
        copied_attack_phy.direction = self.direction
        copied_attack_phy.rect = self.rect
        return copied_attack_phy

    def set_attack_rect(self, start_pos, direction):
        self.rect = pg.Rect(start_pos[0], start_pos[1], self.attack_size[0], self.attack_size[1])
        self.direction = direction
