import pygame as pg


class SwordLikeAttackPhysics:
    def __init__(self, attack_size):
        self.attack_size = attack_size
        self.attack_rect = None

    def set_attack_rect(self, start_pos):
        self.attack_rect = pg.Rect(start_pos[0], start_pos[1], self.attack_size[0], self.attack_size[1])
