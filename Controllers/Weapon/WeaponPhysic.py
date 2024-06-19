from Controllers.Weapon.AttackPhysic import SwordAttackPhysics, AttackPhysic


class WeaponPhysic:
    def __init__(self):
        self.attack_physic: AttackPhysic


class SwordPhysic(WeaponPhysic):
    def __init__(self, attack_size, damage_types):
        super().__init__()
        self.attack_physic = SwordAttackPhysics(attack_size, damage_types)

    def copy_for_save(self):
        return SwordPhysic(self.attack_physic.attack_size, self.attack_physic.damage_types)