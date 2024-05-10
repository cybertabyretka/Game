class EntityV:
    def __init__(self, asset):
        self.image_up = asset.base_player_asset['up']
        self.image_down = asset.base_player_asset['down']
        self.image_right = asset.base_player_asset['right']
        self.image_left = asset.base_player_asset['left']
        self.current_image = self.image_up

    def rotate(self, rotation):
        if rotation == 0:
            self.current_image = self.image_up
        elif rotation == 90:
            self.current_image = self.image_right
        elif rotation == 180:
            self.current_image = self.image_down
        elif rotation == 270:
            self.current_image = self.image_left

    def render(self, surface, pos):
        surface.blit(self.current_image, pos)

    @staticmethod
    def clear_surface(surface, base_colour=(0, 0, 0)):
        surface.fill(base_colour)
