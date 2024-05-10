from Views.Weapon import WeaponV
from Controllers.WeaponPhysic import SwordLikePhysic


class Weapon:
    def __init__(self, name, animation_asset):
        self.name = name
        self.weapon_view = WeaponV(animation_asset)
        self.physic = SwordLikePhysic()


class SwordLike(Weapon):
    pass
