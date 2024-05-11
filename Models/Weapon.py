from Views.Weapon import WeaponV
from Controllers.WeaponPhysic import SwordLikePhysic


class Weapon:
    def __init__(self, name, animation_asset_dict):
        self.name = name
        self.weapon_view = WeaponV(animation_asset_dict)
        self.physic = SwordLikePhysic()


class SwordLike(Weapon):
    pass
