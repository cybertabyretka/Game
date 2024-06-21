from Controllers.Weapon.WeaponPhysic import StaffPhysic

from Models.Item.Weapons.Weapon import Weapon


class Staff(Weapon):
    def __init__(self, name: str, size: tuple[int, int], icon, paths_asset: dict[str, str], buttons, projectile):
        super().__init__(name, size, icon, paths_asset, buttons)
        self.physic = StaffPhysic(projectile)

    def attack(self, room, direction, entity, state):
        pos = self.set_animation(direction, entity)
        if self.view.copied_animation is not None:
            copied_attack_physic = self.physic.attack_physic.copy()
            copied_attack_physic.set_attack_rect(pos, direction)
            copied_attack_physic.view.download_images()
            room.collisions_map.movable_damage_map.append(copied_attack_physic)
            return True
        return False

    def copy_for_save(self):
        return Staff(self.name, self.size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons, self.physic.attack_physic.projectile.copy_for_save())