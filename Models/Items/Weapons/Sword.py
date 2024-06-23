from Controllers.Weapons.WeaponPhysic import SwordPhysic
from Controllers.Entities.States.AbstractStates.NPCAbstractState import NPCAbstractState
from Controllers.Entities.States.AbstractStates.PlayerAbstractState import PlayerAbstractState

from Models.InteractionObjects.Button import Button
from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Room.Room import Room
from Models.Entities.BaseEntity import Entity

from Views.Items.ItemIcon import Icon


class Sword(Weapon):
    def __init__(self, name: str, size: tuple[int, int], icon: Icon, paths_asset: dict[str, str], buttons: list[Button], attack_size: tuple[int, int], damage_types: dict[str, int]):
        super().__init__(name, size, icon, paths_asset, buttons)
        self.physic: SwordPhysic = SwordPhysic(attack_size, damage_types)

    def try_attack(self, room: Room, direction: int, entity, state: NPCAbstractState | PlayerAbstractState) -> bool:
        pos = self.set_animation(direction, entity)
        if self.view.copied_animation is not None:
            copied_attack_physic = self.physic.attack_physic.copy()
            copied_attack_physic.set_attack_rect(pos, direction)
            room.collisions_map.add_damage(copied_attack_physic, id(copied_attack_physic))
            state.copied_damage_physic = copied_attack_physic
            return True
        return False

    def copy_for_save(self):
        return Sword(self.name, self.size, self.view.icon.copy_for_save(), self.view.paths_asset, self.buttons, self.physic.attack_physic.attack_size, self.physic.attack_physic.damage_types)