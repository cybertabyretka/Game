from Utils.Image import load_image
from Utils.Settings.Paths import BASE_PATH


EMPTY_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/empty_icon.png', set_colour=True, colour_to_change=(120, 0, 12))
SWORD_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/Weapons/SwordLike/Sword/Icon/sword.png', set_colour=True, colour_to_change=(120, 0, 12))
SHIELD_ICON = load_image(BASE_PATH + 'Data/Images/Game/Items/Shields/BaseShield/Icon/shield.png', set_colour=True, colour_to_change=(120, 0, 12))