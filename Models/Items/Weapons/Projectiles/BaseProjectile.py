from Views.Items.Projectiles.BaseProjectile import BaseProjectileV


class BaseProjectile:
    def __init__(self, image_path: str, damage_types: dict[str, int], size: tuple[int, int], max_velocity: int, physic_type, view_type):
        self.physic = physic_type(size, max_velocity, damage_types)
        self.view = view_type(image_path)

    def copy(self):
        pass

    def set_attack_rect(self, start_pos: tuple[int, int], direction: int):
        self.physic.set_attack_rect(start_pos, direction)

    def copy_for_save(self):
        pass