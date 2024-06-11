class EntityV:
    def __init__(self, asset, surface):
        self.image_up = asset.base_player_asset['up']
        self.image_down = asset.base_player_asset['down']
        self.image_right = asset.base_player_asset['right']
        self.image_left = asset.base_player_asset['left']
        self.current_image = self.image_up
        self.surface = surface
        self.surface.set_colorkey((0, 0, 0))

    def rotate(self, rotation):
        if rotation == 0:
            self.current_image = self.image_up
        elif rotation == 90:
            self.current_image = self.image_right
        elif rotation == 180:
            self.current_image = self.image_down
        elif rotation == 270:
            self.current_image = self.image_left

    def render(self, pos):
        self.surface.blit(self.current_image, pos)

    def clear_surface(self, base_colour=(0, 0, 0)):
        self.surface.fill(base_colour)


def render_entities(NPCs, player, surface, base_colour=(0, 0, 0)):
    surface.fill(base_colour)
    for NPC in NPCs:
        NPC.states_stack.peek().draw()
    player.states_stack.peek().draw()