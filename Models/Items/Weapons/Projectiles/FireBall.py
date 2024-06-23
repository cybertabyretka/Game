from Controllers.Weapons.Projectiles.FireBallPhysic import FireBallPhysic

from Views.Items.Projectiles.FireBall import FireBallV

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile


class FireBall(BaseProjectile):
    def __init__(self, image_path: str, damage_types: dict[str, int], size: tuple[int, int], max_velocity: int):
        super().__init__(image_path, damage_types, size, max_velocity, FireBallPhysic, FireBallV)

    def copy(self):
        return FireBall(self.view.path, self.physic.damage_types, (self.physic.collision.rect.w, self.physic.collision.rect.h), self.physic.max_velocity)

    def copy_for_save(self):
        return FireBall(self.view.path, self.physic.damage_types, (self.physic.collision.rect.w, self.physic.collision.rect.h), self.physic.max_velocity)