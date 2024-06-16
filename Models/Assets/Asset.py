from Utils.Image import load_images, load_image
from Utils.Setting import BASE_PATH
from Utils.Animation import Animation

from Models.Assets.PathsAsset import *


class TilesAssets:
    def __init__(self):
        self.base_map_asset = {'floor': load_images(TILES['floor']),
                               'front_wall': load_images(TILES['front_wall']),
                               'side_wall': load_images(TILES['side_wall']),
                               'front_door': load_images(TILES['front_door']),
                               'side_door': load_images(TILES['side_door'])}


class PlayerAssets:
    def __init__(self):
        self.base_player_asset = {'up': load_image(PLAYER['up']),
                                  'down': load_image(PLAYER['down']),
                                  'left': load_image(PLAYER['left']),
                                  'right': load_image(PLAYER['right'])}


class WeaponsAssets:
    def __init__(self):
        self.sword_asset = {'animation_up': Animation(load_images(SWORD['animation_up'], set_colour=True), 1, False),
                            'animation_down': Animation(load_images(SWORD['animation_down'], set_colour=True), 1, False),
                            'animation_left': Animation(load_images(SWORD['animation_left'], set_colour=True), 1, False),
                            'animation_right': Animation(load_images(SWORD['animation_right'], set_colour=True), 1, False)}
