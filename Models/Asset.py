from Utils.Picture import load_images
from Utils.Setting import BASE_PATH
from Utils.Animation import Animation


class TilesAssets:
    def __init__(self):
        self.base_map_asset = {'tile_size': 35,
                               'floor': load_images(BASE_PATH + 'Data/Environment/Floors'),
                               'front_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Front'),
                               'side_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Side')}


class AnimationAssets:
    def __init__(self, game_fps):
        self.weapon_assets = {'sword': Animation(load_images(BASE_PATH + ''), 1, False, game_fps),
                              }
