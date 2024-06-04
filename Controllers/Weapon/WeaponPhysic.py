from Controllers.Weapon.AttackPhysic import SwordLikeAttackPhysics


class SwordLikePhysic:
    def __init__(self, attack_size):
        self.attack_physic = SwordLikeAttackPhysics(attack_size)