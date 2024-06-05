import pygame as pg


class SwordLikeAttackPhysics:
    def __init__(self, attack_size):
        self.direction = None
        self.attack_size = attack_size
        self.rect = None

    def set_attack_rect(self, start_pos, direction):
        self.rect = pg.Rect(start_pos[0], start_pos[1], self.attack_size[0], self.attack_size[1])
        self.direction = direction
