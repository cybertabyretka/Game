from Views.Items.Projectiles.BaseProjectile import BaseProjectileV


class BaseProjectile:
    def __init__(self, image_path, damage_types, size, max_velocity, physic_type, view_type):
        self.physic = physic_type(size, max_velocity, damage_types)
        self.view = view_type(image_path)

    def copy(self):
        pass

    def set_attack_rect(self, start_pos, direction):
        self.physic.set_attack_rect(start_pos, direction)

    def copy_for_save(self):
        pass