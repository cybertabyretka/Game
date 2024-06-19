from Models.Item.Weapons.Weapon import Weapon
from Models.Button import Button

from Controllers.Weapon.WeaponPhysic import SwordPhysic

from Views.Item.ItemIcon import Icon


class Sword(Weapon):
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, paths_asset: dict[str, str], buttons: list[Button], attack_size, damage_types):
        super().__init__(name, size, icon, paths_asset, buttons)
        self.physic = SwordPhysic(attack_size, damage_types)

    def attack(self, room, direction, entity, state):
        pos = self.set_animation(direction, entity)
        if self.view.copied_animation is not None:
            copied_attack_physic = self.physic.attack_physic.copy()
            copied_attack_physic.set_attack_rect(pos, direction)
            room.collisions_map.add_damage(copied_attack_physic, id(copied_attack_physic))
            state.copied_damage_rect = copied_attack_physic
            return True
        return False

    def copy_for_save(self):
        return Sword(self.name, self.size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons, self.physic.attack_size, self.physic.damage_types)