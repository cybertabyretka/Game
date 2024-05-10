from Utils.Picture import load_images
from Utils.Picture import load_image
from Utils.Setting import BASE_PATH
from Utils.Animation import Animation


class TilesAssets:
    def __init__(self):
        self.base_map_asset = {'tile_size': (35, 35),
                               'floor': load_images(BASE_PATH + 'Data/Environment/Floors'),
                               'front_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Front'),
                               'side_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Side')}


class PlayerAssets:
    def __init__(self):
        self.base_player_asset = {'tile_size': (35, 35),
                                  'up': load_image(BASE_PATH + 'Data/Entities/Player/Images/player_up.png'),
                                  'down': load_image(BASE_PATH + 'Data/Entities/Player/Images/player_down.png'),
                                  'left': load_image(BASE_PATH + 'Data/Entities/Player/Images/player_left.png'),
                                  'right': load_image(BASE_PATH + 'Data/Entities/Player/Images/player_right.png')}


class WeaponsAssets:
    def __init__(self, game_fps):
        self.sword_asset = {'tile_size': (20, 20),
                            'animation': Animation(load_images(BASE_PATH + 'Data/Weapons/SwordLike/Sword', set_colour=True), 1, False, game_fps)}
