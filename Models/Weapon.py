from Views.Weapon import WeaponV
from Controllers.Weapon.WeaponPhysic import SwordLikePhysic


class Weapon:
    def __init__(self, name, size, attack_size, animation_asset_dict):
        self.name = name
        self.size = size
        self.weapon_view = WeaponV(animation_asset_dict)
        self.physic = SwordLikePhysic(attack_size)

    def set_animation(self, rotation, entity):
        pos = (0, 0)
        if rotation == 0:
            pos = (entity.physic.collision.rect.x, entity.physic.collision.rect.y - entity.physic.collision.rect.height)
        elif rotation == 90:
            pos = (entity.physic.collision.rect.x + entity.physic.collision.rect.width, entity.physic.collision.rect.y)
        elif rotation == 180:
            pos = (entity.physic.collision.rect.x, entity.physic.collision.rect.y + entity.physic.collision.rect.height)
        elif rotation == 270:
            pos = (entity.physic.collision.rect.x - entity.physic.collision.rect.width, entity.physic.collision.rect.y)
        self.physic.attack_physic.set_attack_rect(pos, rotation)
        self.weapon_view.set_animation(rotation, pos)


class SwordLike(Weapon):
    pass
