import pygame as pg

from Controllers.RoomMap.RoomsMapUtils import make_room
from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, TILE_SIZE
from BaseVariables.Buttons.Buttons import WEAPONS_CHANGE_BUTTON, SHIELD_CHANGE_BUTTON
from BaseVariables.Paths import FONT_PATH
from Constants.Colours import WHITE_RGB, DARK_GRAY_RGB

from BaseVariables.Assets.PathsAsset import *
from Models.Room.RoomsMap import RoomsMap
from Models.Room.Door import Door
from Models.Entities.Player import Player
from Models.Entities.NPCs.Swordsman import Swordsman
from Models.Item.Weapons.Sword import Sword
from Models.Room.Tile import Tile
from Models.Inventory.Inventory import Inventory
from Models.InteractionObjects.InGameWindow import InGameWindow
from Models.Text import Text
from Models.Item.Shield import Shield
from Models.Entities.NPCs.Wizard import Wizard
from Models.Item.Weapons.Staff import Staff
from Models.Item.Weapons.Projectiles.FireBall import FireBall

from Views.Item.ItemIcon import Icon


entities_surface = pg.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))

sword_icon = Icon(SWORD['icon'])
player_sword = Sword('Base sword', (30, 30), sword_icon, SWORD, [WEAPONS_CHANGE_BUTTON], (35, 35), {'cut': 1})
swordsman_sword = Sword('Base sword', (30, 30), sword_icon, SWORD, [WEAPONS_CHANGE_BUTTON], (35, 35), {'cut': 1})

shield_icon = Icon(SHIELD['icon'])
player_shield = Shield('Base shield', (30, 30), shield_icon, [SHIELD_CHANGE_BUTTON], {'cut': 2})
swordsman_shield = Shield('Base shield', (30, 30), shield_icon, [SHIELD_CHANGE_BUTTON], {'cut': 2})

staff_icon = Icon(STAFF['icon'])
fire_ball = FireBall(FIRE_BALL['image'], {'fire': 2}, (30, 30), 1)
wizard_staff = Staff('Base staff', (30, 30), staff_icon, STAFF, [WEAPONS_CHANGE_BUTTON], fire_ball)

wizard_inventory = Inventory((5, 5), (30, 30))
wizard_inventory.place_item((0, 0), wizard_staff)
swordsman_inventory = Inventory((5, 5), (30, 30))
swordsman_inventory.place_items([(0, 0), (1, 0)], [swordsman_sword, swordsman_shield])
player_inventory = Inventory((10, 10), (30, 30))

player_windows = {'inventory_base': InGameWindow(Text('Your inventory', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 100), DARK_GRAY_RGB),
                  'inventory_for_steal': InGameWindow(Text('Loot', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 400), DARK_GRAY_RGB)}

wizard = Wizard(wizard_inventory, WIZARD, start_pos=(140, 560), current_weapon=wizard_staff)
swordsman = Swordsman(swordsman_inventory, SWORDSMAN, start_pos=(140, 595), current_weapon=swordsman_sword, current_shield=swordsman_shield)
NPCs = [swordsman, wizard]

BASE_ROOMS_MAP = RoomsMap((1, 2))
make_room(BASE_ROOMS_MAP.map, (0, 0), NPCs, [])
make_room(BASE_ROOMS_MAP.map, (1, 0), [], [])
doors = [Door(Tile(f'{TILES["front_door"]}/{0}.png', 0, (350, 665)),
              Tile(f'{TILES["front_door"]}/{0}.png', 0, (350, 0)),
              (350, 630), (350, 35))]
doors_connections = {doors[0]: [BASE_ROOMS_MAP.map[0][0], BASE_ROOMS_MAP.map[1][0]]}
BASE_ROOMS_MAP.add_doors_connections(doors_connections)
BASE_ROOMS_MAP.add_doors()

BASE_PLAYER_START_POS = (120, 120)

for NPC in NPCs:
    NPC.physic.collision.get_collisions_around(BASE_ROOMS_MAP.get_current_room().collisions_map.map, TILE_SIZE)

BASE_PLAYER = Player(player_inventory, player_windows, PLAYER, start_pos=BASE_PLAYER_START_POS, current_weapon=player_sword, current_shield=player_shield)
BASE_PLAYER.physic.collision.get_collisions_around(BASE_ROOMS_MAP.get_current_room().collisions_map.map, TILE_SIZE)
