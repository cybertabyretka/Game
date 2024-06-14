import pygame as pg

from Utils.RoomsMap import connect_rooms, make_room
from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY, TILE_SIZE
from Utils.Settings.Icons import SWORD_ICON, SHIELD_ICON
from Utils.Settings.Buttons.Buttons import SWORD_CHANGE_BUTTON, SHIELD_CHANGE_BUTTON
from Utils.Settings.Paths import FONT_PATH
from Utils.Settings.Colours import WHITE_RGB, DARK_GRAY_RGB

from Models.Room.RoomsMap import RoomsMap
from Models.Room.Door import Door
from Models.Game.Game import Game
from Models.Asset import WeaponsAssets, PlayerAssets, TilesAssets
from Models.Entity.Entity import Swordsman, Player
from Models.Item.Weapon import SwordLike
from Models.Room.Tile import Tile
from Models.Entity.Inventory.Inventory import Inventory
from Models.InGameWindow import InGameWindow
from Models.Text import Text
from Models.Item.Shield import Shield

from Views.Item.ItemIcon import Icon


entities_surface = pg.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))

weapons_assets = WeaponsAssets()
sword_icon = Icon(SWORD_ICON)
player_sword = SwordLike('Base sword', (20, 20), (35, 35), sword_icon, weapons_assets.sword_asset, [SWORD_CHANGE_BUTTON])
swordsman_sword = SwordLike('Base sword', (20, 20), (35, 35), sword_icon, weapons_assets.sword_asset, [SWORD_CHANGE_BUTTON])

shield_icon = Icon(SHIELD_ICON)
player_shield = Shield('Base shield', (20, 20), shield_icon, 2, ['sword'], [SHIELD_CHANGE_BUTTON])
swordsman_shield = Shield('Base shield', (20, 20), shield_icon, 2, ['sword'], [SHIELD_CHANGE_BUTTON])

player_asset = PlayerAssets()

swordsman_inventory = Inventory((5, 5), (30, 30))
swordsman_inventory.place_items([(0, 0), (1, 0)], [swordsman_sword, swordsman_shield])
player_inventory = Inventory((10, 10), (30, 30))

player_windows = {'inventory_base': InGameWindow(Text('Your inventory', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 100), DARK_GRAY_RGB),
                  'inventory_for_steal': InGameWindow(Text('Loot', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 400), DARK_GRAY_RGB)}

swordsman = Swordsman(player_asset, entities_surface, swordsman_inventory, start_pos=(140, 595), current_weapon=swordsman_sword, current_shield=swordsman_shield)
NPCs = [swordsman]

BASE_ROOMS_MAP = RoomsMap((1, 2))
make_room(BASE_ROOMS_MAP.map, (0, 0), DISPLAY.surface, NPCs)
make_room(BASE_ROOMS_MAP.map, (1, 0), DISPLAY.surface, [])
doors = [Door(Tile(TilesAssets().doors['front_door'][0], 0, (350, 0)),
              Tile(TilesAssets().doors['front_door'][0], 0, (350, 665)),
              BASE_ROOMS_MAP.map[0][0], BASE_ROOMS_MAP.map[1][0],
              (350, 35), (350, 630))]
connect_rooms(doors[0])

BASE_PLAYER_START_POS = (120, 120)

for NPC in NPCs:
    NPC.physic.collision.get_collisions_around(BASE_ROOMS_MAP.get_current_room().collisions_map.map, TILE_SIZE)

BASE_PLAYER = Player(player_asset, entities_surface, player_inventory, player_windows, start_pos=BASE_PLAYER_START_POS, current_weapon=player_sword, current_shield=player_shield)
BASE_PLAYER.physic.collision.get_collisions_around(BASE_ROOMS_MAP.get_current_room().collisions_map.map, TILE_SIZE)

BASE_GAME = Game(DISPLAY, BASE_ROOMS_MAP, BASE_PLAYER)