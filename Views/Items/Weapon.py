from Views.Items.Item import ItemV

from Views.Animation import Animation
from Utils.Image import load_images


class WeaponV(ItemV):
    def __init__(self, icon, paths_asset):
        super().__init__(icon)
        self.paths_asset = paths_asset
        self.copied_animation = None
        self.animation_asset = {}

    def download_images(self):
        self.animation_asset['animation_up'] = Animation(load_images(self.paths_asset['animation_up'], set_colour=True), 1, False)
        self.animation_asset['animation_down'] = Animation(load_images(self.paths_asset['animation_down'], set_colour=True), 1, False)
        self.animation_asset['animation_left'] = Animation(load_images(self.paths_asset['animation_left'], set_colour=True), 1, False)
        self.animation_asset['animation_right'] = Animation(load_images(self.paths_asset['animation_right'], set_colour=True), 1, False)
        self.icon.download_images()

    def set_animation(self, rotation, pos):
        if rotation == 0:
            self.copied_animation = self.animation_asset['animation_up'].copy()
        elif rotation == 90:
            self.copied_animation = self.animation_asset['animation_right'].copy()
        elif rotation == 180:
            self.copied_animation = self.animation_asset['animation_down'].copy()
        elif rotation == 270:
            self.copied_animation = self.animation_asset['animation_left'].copy()
        if self.copied_animation is not None:
            self.copied_animation.pos = pos

    def draw_animation(self, surface):
        self.copied_animation.draw(surface)

    def get_pos(self):
        return self.copied_animation.pos