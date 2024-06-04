class WeaponV:
    def __init__(self, animation_asset_dict):
        self.animation_asset_dict = animation_asset_dict
        self.copied_animation = None

    def set_animation(self, rotation, pos):
        if rotation == 0:
            self.copied_animation = self.animation_asset_dict['animation_up'].copy()
        elif rotation == 90:
            self.copied_animation = self.animation_asset_dict['animation_right'].copy()
        elif rotation == 180:
            self.copied_animation = self.animation_asset_dict['animation_down'].copy()
        elif rotation == 270:
            self.copied_animation = self.animation_asset_dict['animation_left'].copy()
        self.copied_animation.pos = pos

    def render(self, surface):
        self.copied_animation.render(surface)

    def get_pos(self):
        return self.copied_animation.pos