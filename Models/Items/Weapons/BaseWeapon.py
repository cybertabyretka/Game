from Controllers.Weapons.WeaponPhysic import WeaponPhysic

from Models.InteractionObjects.Button import Button
from Models.Items.Item import Item

from Views.Items.ItemIcon import Icon
from Views.Items.Weapon import WeaponV


class Weapon(Item):
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, paths_asset: dict[str, str], buttons: list[Button]):
        super().__init__(name, size, icon, buttons)
        self.view: WeaponV = WeaponV(icon, paths_asset)
        self.physic: WeaponPhysic

    def copy_for_save(self):
        return Weapon(self.name, self.size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons)

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
        self.view.set_animation(rotation, pos)
        return pos
