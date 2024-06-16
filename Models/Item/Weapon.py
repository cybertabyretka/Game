from Views.Item.Weapon import WeaponV

from Controllers.Weapon.WeaponPhysic import SwordLikePhysic

from Models.Item.Item import Item


class Weapon(Item):
    def __init__(self, name, size, attack_size, icon, paths_asset, buttons):
        super().__init__(name, size, icon, buttons)
        self.view = WeaponV(icon, paths_asset)
        self.physic = SwordLikePhysic(attack_size)

    def copy_for_save(self):
        return Weapon(self.name, self.size, self.physic.attack_physic.attack_size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons)

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
        self.view.set_animation(rotation, pos)


class SwordLike(Weapon):
    pass
