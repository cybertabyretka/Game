from Controllers.Weapon.Projectiles.FireBallPhysic import FireBallPhysic

from Views.Item.Projectiles.FireBall import FireBallV


class FireBall:
    def __init__(self, image_path, damage_types, size, max_velocity):
        self.physic = FireBallPhysic(size, max_velocity, damage_types)
        self.view = FireBallV(image_path)

    def copy(self):
        copied_fire_ball = FireBall(self.view.path, self.physic.damage_types, (self.physic.collision.rect.w, self.physic.collision.rect.h), self.physic.max_velocity)
        copied_fire_ball.physic = self.physic
        copied_fire_ball.view = self.view
        return copied_fire_ball

    def set_attack_rect(self, start_pos, direction):
        self.physic.set_attack_rect(start_pos, direction)

    def copy_for_save(self):
        return FireBall(self.view.path, self.physic.damage_types, (self.physic.rect.w, self.physic.rect.h), self.physic.max_velocity)