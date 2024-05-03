from Utils.Image import load_images
from Utils.Setting import BASE_PATH


class TilesAssets:
    def __init__(self):
        self.base_asset = {'tile_size': 35,
                           'floor': load_images(BASE_PATH + 'Data/Environment/Floors'),
                           'front_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Front'),
                           'side_wall': load_images(BASE_PATH + 'Data/Environment/Walls/Side')}
