from Views.Weapon import WeaponV
from Controllers.WeaponPhysic import SwordLikePhysic


class Weapon:
    def __init__(self, name, animation):
        self.name = name
        self.weapon_view = WeaponV(animation)


class SwordLike(Weapon):
    pass
