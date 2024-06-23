from Controllers.Weapons.AttackPhysic import SwordAttackPhysics, AttackPhysic, StaffAttackPhysic

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile


class WeaponPhysic:
    def __init__(self):
        self.attack_physic: AttackPhysic


class SwordPhysic(WeaponPhysic):
    def __init__(self, attack_size: tuple[int, int], damage_types: dict[str, int]):
        super().__init__()
        self.attack_physic: SwordAttackPhysics = SwordAttackPhysics(attack_size, damage_types)

    def copy_for_save(self):
        return SwordPhysic(self.attack_physic.attack_size, self.attack_physic.damage_types)


class StaffPhysic(WeaponPhysic):
    def __init__(self, projectile: BaseProjectile):
        super().__init__()
        self.attack_physic: StaffAttackPhysic = StaffAttackPhysic(projectile)

    def copy_for_save(self):
        return StaffPhysic(self.attack_physic.projectile)