from Utils.Settings.Paths import BASE_PATH
from Utils.Settings.Icons.IconsPaths import *


TILES: dict[str, str] = {'floor': BASE_PATH + 'Data/Images/Game/Environment/Floors',
                         'front_wall': BASE_PATH + 'Data/Images/Game/Environment/Walls/Front',
                         'side_wall': BASE_PATH + 'Data/Images/Game/Environment/Walls/Side',
                         'front_door': BASE_PATH + 'Data/Images/Game/Environment/Doors/Front',
                         'side_door': BASE_PATH + 'Data/Images/Game/Environment/Doors/Side'}

PLAYER: dict[str, str] = {'up': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png',
                          'down': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png',
                          'left': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png',
                          'right': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png'}

WIZARD: dict[str, str] = {'up': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png',
                          'down': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png',
                          'left': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png',
                          'right': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png'}

SWORDSMAN: dict[str, str] = {'up': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png',
                             'down': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png',
                             'left': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png',
                             'right': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png'}

SWORD: dict[str, str] = {'animation_up': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Up',
                         'animation_down': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Down',
                         'animation_left': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Left',
                         'animation_right': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Right',
                         'icon': SWORD_ICON_PATH}

SHIELD: dict[str, str] = {'icon': SHIELD_ICON_PATH}

STAFF: dict[str, str] = {'animation_up': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Up',
                         'animation_down': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Down',
                         'animation_left': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Left',
                         'animation_right': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Right',
                         'icon': STAFF_ICON_PATH}

FIRE_BALL: dict[str, str] = {'image': FIRE_BALL_ICON_PATH}

EMPTY_ITEM: dict[str, str] = {'icon': EMPTY_ICON_PATH}