from Utils.Image import load_image


class EntityV:
    def __init__(self, paths_asset):
        self.paths_asset = paths_asset
        self.image_up = None
        self.image_down = None
        self.image_right = None
        self.image_left = None
        self.current_image = None

    def download_images(self, current_weapon, current_shield, inventory):
        self.image_up = load_image(self.paths_asset['up'])
        self.image_down = load_image(self.paths_asset['down'])
        self.image_right = load_image(self.paths_asset['right'])
        self.image_left = load_image(self.paths_asset['left'])
        self.current_image = self.image_up
        if current_weapon is not None:
            current_weapon.view.download_images()
        if current_shield is not None:
            current_shield.view.download_images()
        inventory.download_images()

    def rotate(self, rotation):
        if rotation == 0:
            self.current_image = self.image_up
        elif rotation == 90:
            self.current_image = self.image_right
        elif rotation == 180:
            self.current_image = self.image_down
        elif rotation == 270:
            self.current_image = self.image_left

    def draw(self, surface, pos):
        surface.blit(self.current_image, pos)
