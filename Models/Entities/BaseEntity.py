from Models.HealthBar import HealthBar
from Models.Items.Weapons.BaseWeapon import Weapon
from Models.Items.Shield import Shield
from Models.Inventory.Inventory import Inventory

from Constants.StatesNames import IDLE_STATE

from DataStructures.Stack import Stack

from Views.Entities.Entity import EntityV


class Entity:
    def __init__(self, width: int, height: int, start_pos: tuple[int, int], max_velocity: int, current_weapon: Weapon | None, current_shield: Shield | None, max_health: int, current_health: int, inventory: Inventory, paths_asset: dict[str, str], physic_type, states_types):
        self.view: EntityV = EntityV(paths_asset)
        self.physic = physic_type(width, height, start_pos, max_velocity)
        self.states_stack: Stack = Stack(states_types[IDLE_STATE](self))
        self.current_weapon: Weapon | None = current_weapon
        self.current_shield: Shield | None = current_shield
        self.health: HealthBar = HealthBar(max_health, current_health)
        self.inventory: Inventory = inventory
        self.states_types = states_types
