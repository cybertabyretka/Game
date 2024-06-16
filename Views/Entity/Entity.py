from Utils.Image import load_image


class EntityV:
    def __init__(self, paths_asset):
        self.paths_asset = paths_asset
        self.image_up = None
        self.image_down = None
        self.image_right = None
        self.image_left = None
        self.current_image = self.image_up

    def download_images(self):
        self.image_up = load_image(self.paths_asset['up'])
        self.image_down = load_image(self.paths_asset['down'])
        self.image_right = load_image(self.paths_asset['right'])
        self.image_left = load_image(self.paths_asset['left'])

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


def render_entities(NPCs, player, surface, base_colour=(0, 0, 0)):
    surface.fill(base_colour)
    for NPC in NPCs:
        NPC.states_stack.peek().draw()
    player.states_stack.peek().draw()


def clear_surface(surface, base_colour=(0, 0, 0)):
    surface.fill(base_colour)


class PlayerV(EntityV):
    def __init__(self, windows, paths_asset):
        super().__init__(paths_asset)
        self.windows = windows
