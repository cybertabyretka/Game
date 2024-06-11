from Utils.Image import load_images, load_image
from Utils.Setting import BASE_PATH
from Utils.Animation import Animation


class TilesAssets:
    def __init__(self):
        self.base_map_asset = {'tile_size': (35, 35),
                               'floor': load_images(BASE_PATH + 'Data/Images/Game/Environment/Floors'),
                               'front_wall': load_images(BASE_PATH + 'Data/Images/Game/Environment/Walls/Front'),
                               'side_wall': load_images(BASE_PATH + 'Data/Images/Game/Environment/Walls/Side')}


class PlayerAssets:
    def __init__(self):
        self.base_player_asset = {'tile_size': (35, 35),
                                  'up': load_image(BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png'),
                                  'down': load_image(BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png'),
                                  'left': load_image(BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png'),
                                  'right': load_image(BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png')}


class WeaponsAssets:
    def __init__(self):
        self.sword_asset = {'tile_size': (35, 35),
                            'animation_up': Animation(load_images(BASE_PATH + 'Data/Images/Game/Weapons/SwordLike/Sword/Up', set_colour=True), 1, False),
                            'animation_down': Animation(load_images(BASE_PATH + 'Data/Images/Game/Weapons/SwordLike/Sword/Down', set_colour=True), 1, False),
                            'animation_left': Animation(load_images(BASE_PATH + 'Data/Images/Game/Weapons/SwordLike/Sword/Left', set_colour=True), 1, False),
                            'animation_right': Animation(load_images(BASE_PATH + 'Data/Images/Game/Weapons/SwordLike/Sword/Right', set_colour=True), 1, False)}
