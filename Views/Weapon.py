class WeaponV:
    def __init__(self, animation_asset_dict):
        self.animation_asset_dict = animation_asset_dict
        self.copied_animation = None

    def set_animation(self, rotation, player):
        if rotation == 0:
            self.copied_animation = self.animation_asset_dict['animation_up'].copy()
            self.copied_animation.pos = (player.physic.collision.rect.x + (player.physic.collision.rect.width // 2), player.physic.collision.rect.y)
        elif rotation == 90:
            self.copied_animation = self.animation_asset_dict['animation_right'].copy()
            self.copied_animation.pos = (player.physic.collision.rect.x + player.physic.collision.rect.width, player.physic.collision.rect.y + (player.physic.collision.rect.height // 2))
        elif rotation == 180:
            self.copied_animation = self.animation_asset_dict['animation_down'].copy()
            self.copied_animation.pos = (player.physic.collision.rect.x + (player.physic.collision.rect.width // 2), player.physic.collision.rect.y + player.physic.collision.rect.height)
        elif rotation == 270:
            self.copied_animation = self.animation_asset_dict['animation_left'].copy()
            self.copied_animation.pos = (player.physic.collision.rect.x, player.physic.collision.rect.y + (player.physic.collision.rect.height // 2))