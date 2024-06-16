from Utils.Settings.Paths import BASE_PATH
from Utils.Settings.Icons.IconsPaths import SWORD_ICON_PATH, SHIELD_ICON_PATH, EMPTY_ICON_PATH


TILES = {'floor': BASE_PATH + 'Data/Images/Game/Environment/Floors',
         'front_wall': BASE_PATH + 'Data/Images/Game/Environment/Walls/Front',
         'side_wall': BASE_PATH + 'Data/Images/Game/Environment/Walls/Side',
         'front_door': BASE_PATH + 'Data/Images/Game/Environment/Doors/Front',
         'side_door': BASE_PATH + 'Data/Images/Game/Environment/Doors/Side'}

PLAYER = {'up': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png',
          'down': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png',
          'left': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png',
          'right': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png'}

SWORDSMAN = {'up': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_up.png',
             'down': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_down.png',
             'left': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_left.png',
             'right': BASE_PATH + 'Data/Images/Game/Entities/Player/Images/player_right.png'}

SWORD = {'animation_up': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Up',
         'animation_down': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Down',
         'animation_left': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Left',
         'animation_right': BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Right',
         'icon': SWORD_ICON_PATH}

SHIELD = {'icon': SHIELD_ICON_PATH}

EMPTY_ITEM = {'icon': EMPTY_ICON_PATH}