import pygame as pg

from BaseVariables.PathsAsset import *
from BaseVariables.Buttons.Buttons import WEAPONS_CHANGE_BUTTON, SHIELD_CHANGE_BUTTON
from BaseVariables.Paths import *
from BaseVariables.Others import TILE_SIZE

from Views.Display import Display
from Views.Items.ItemIcon import Icon

from Constants.Colours import WHITE_RGB, DARK_GRAY_RGB
from Constants.Display import *
from Constants.DamageTypes import *

from Controllers.RoomMap.RoomsMapUtils import make_room, create_tile_map
from Controllers.Entities.Physic.GetCollisionsAround import get_collisions_around

from Models.Room.Room import Room
from Models.Entities.NPCs.BaseNPC import NPC
from Models.Entities.NPCs.Swordsman import Swordsman
from Models.Entities.NPCs.Wizard import Wizard
from Models.Entities.Player import Player
from Models.InteractionObjects.InGameWindow import InGameWindow
from Models.Inventory.Inventory import Inventory
from Models.Items.Shield import Shield
from Models.Items.Weapons.Projectiles.FireBall import FireBall
from Models.Items.Weapons.Staff import Staff
from Models.Items.Weapons.Sword import Sword
from Models.Room.Door import Door
from Models.Room.RoomsMap import RoomsMap
from Models.Room.Tile import Tile
from Models.Text import Text

from Utils.Image import load_image


DISPLAY: Display = Display(DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME)

BACKGROUND_PICTURE: pg.Surface = load_image(BASE_PATH + 'ReadyData/Images/MainMenu/background.png')

sword_icon: Icon = Icon(SWORD['icon'])
player_sword: Sword = Sword('Base sword', (30, 30), sword_icon, SWORD, [WEAPONS_CHANGE_BUTTON], (35, 35), {'cut': 1})
swordsman_sword: Sword = Sword('Base sword', (30, 30), sword_icon, SWORD, [WEAPONS_CHANGE_BUTTON], (35, 35), {'cut': 1})

shield_icon: Icon = Icon(SHIELD['icon'])
player_shield: Shield = Shield('Base shield', (30, 30), shield_icon, [SHIELD_CHANGE_BUTTON], {CUT: 2})
swordsman_shield: Shield = Shield('Base shield', (30, 30), shield_icon, [SHIELD_CHANGE_BUTTON], {CUT: 2})

staff_icon: Icon = Icon(STAFF['icon'])
fire_ball: FireBall = FireBall(FIRE_BALL['image'], {FIRE: 2}, (30, 30), 1)
wizard_staff: Staff = Staff('Base staff', (30, 30), staff_icon, STAFF, [WEAPONS_CHANGE_BUTTON], fire_ball)

wizard_inventory: Inventory = Inventory((5, 5), (30, 30))
wizard_inventory.place_item((0, 0), wizard_staff)
swordsman_inventory: Inventory = Inventory((5, 5), (30, 30))
swordsman_inventory.place_items([(0, 0), (1, 0)], [swordsman_sword, swordsman_shield])
player_inventory: Inventory = Inventory((10, 10), (30, 30))

player_windows: dict[str, InGameWindow] = {'inventory_base': InGameWindow(Text('Your inventory', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 100), DARK_GRAY_RGB),
                                           'inventory_for_steal': InGameWindow(Text('Loot', WHITE_RGB, 15, FONT_PATH), (300, 315), (200, 400), DARK_GRAY_RGB)}

wizard: WIZARD = Wizard(wizard_inventory, WIZARD, start_pos=(140, 560), current_weapon=wizard_staff)
swordsman: Swordsman = Swordsman(swordsman_inventory, SWORDSMAN, start_pos=(140, 595), current_weapon=swordsman_sword, current_shield=swordsman_shield)

tiles = [Tile(f'{TILES["front_wall"]}/0.png', 0, (70, 140)), Tile(f'{TILES["front_wall"]}/0.png', 0, (70, 175)), Tile(f'{TILES["front_wall"]}/0.png', 0, (105, 175))]
tile_map = create_tile_map(tiles)
BASE_ROOMS_MAP: RoomsMap = RoomsMap((2, 2))
make_room(BASE_ROOMS_MAP.map, (0, 0), [swordsman], [])
make_room(BASE_ROOMS_MAP.map, (0, 1), [], [])
make_room(BASE_ROOMS_MAP.map, (1, 0), [wizard], [], tile_map=tile_map)
doors: list[Door] = [Door(Tile(f'{TILES["side_door"]}/0.png', 0, (665, 350)),
                          Tile(f'{TILES["side_door"]}/0.png', 0, (0, 350)),
                          (630, 350), (35, 350)),
                     Door(Tile(f'{TILES["front_door"]}/0.png', 0, (350, 665)),
                          Tile(f'{TILES["front_door"]}/0.png', 0, (350, 0)),
                          (350, 630), (350, 35))]
doors_connections: dict[Door, tuple[Room, Room]] = {doors[0]: (BASE_ROOMS_MAP.map[0][0], BASE_ROOMS_MAP.map[0][1]), doors[1]: (BASE_ROOMS_MAP.map[0][0], BASE_ROOMS_MAP.map[1][0])}
BASE_ROOMS_MAP.add_doors_connections(doors_connections)
BASE_ROOMS_MAP.add_doors()

BASE_PLAYER_START_POS: tuple[int, int] = (120, 120)
for i in range(BASE_ROOMS_MAP.size[0]):
    for j in range(BASE_ROOMS_MAP.size[1]):
        if BASE_ROOMS_MAP.map[i][j] is not None:
            for NPC in BASE_ROOMS_MAP.map[i][j].NPCs:
                get_collisions_around(NPC.physic.collision.rect, TILE_SIZE, BASE_ROOMS_MAP.map[i][j].collisions_map.map, NPC.physic.collision.collisions_around)

BASE_PLAYER: Player = Player(player_inventory, player_windows, PLAYER, start_pos=BASE_PLAYER_START_POS, current_weapon=player_sword, current_shield=player_shield)
get_collisions_around(BASE_PLAYER.physic.collision.rect, TILE_SIZE, BASE_ROOMS_MAP.get_current_room().collisions_map.map, BASE_PLAYER.physic.collision.collisions_around)
