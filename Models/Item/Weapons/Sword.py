from Models.Item.Weapons.Weapon import Weapon
from Models.Button import Button

from Controllers.Weapon.WeaponPhysic import SwordPhysic

from Views.Item.ItemIcon import Icon


class Sword(Weapon):
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, paths_asset: dict[str, str], buttons: list[Button], attack_size, damage_types):
        super().__init__(name, size, icon, paths_asset, buttons)
        self.physic = SwordPhysic(attack_size, damage_types)

    def copy_for_save(self):
        return Sword(self.name, self.size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons, self.physic.attack_size, self.physic.damage_types)