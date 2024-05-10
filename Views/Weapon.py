class WeaponV:
    def __init__(self, animation_asset):
        rotation = 0
        self.animation_asset = animation_asset
        self.copied_animation = None

    def animate(self, surface, pos, rotation):
        self.copied_animation = self.animation_asset.copy()
        surface.blit(self.copied_animation.get_image(), pos)