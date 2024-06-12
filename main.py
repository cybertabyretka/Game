import pygame as pg

pg.init()
pg.font.init()

from Models.Room.Door import Door
from Models.Main import Main
from Models.Game.Game import Game
from Models.Game.MainMenu import MainMenu
from Models.Asset import WeaponsAssets, PlayerAssets, TilesAssets
from Models.Room.RoomsMap import RoomsMap
from Models.Entity.Entity import Swordsman, Player
from Models.Item.Weapon import SwordLike
from Models.Room.Tile import Tile
from Models.Entity.Inventory.Inventory import Inventory
from Models.InGameWindow import InGameWindow
from Models.Text import Text

from Views.Item.ItemIcon import Icon

from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, BACKGROUND_PICTURE, DISPLAY, SWORD_ICON, TILE_SIZE, BASE_PLAYER_START_POS, DARK_GRAY_RGB, WHITE_RGB, FONT_PATH
from Utils.RoomsMap import make_room, connect_rooms

if __name__ == '__main__':
    entities_surface = pg.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    weapons_assets = WeaponsAssets()
    sword_icon = Icon(SWORD_ICON)
    player_sword = SwordLike('Sword', (35, 35), (35, 35), sword_icon, weapons_assets.sword_asset)
    swordsman_sword = SwordLike('Sword', (35, 35), (35, 35), sword_icon, weapons_assets.sword_asset)

    player_asset = PlayerAssets()

    player_inventory = Inventory((10, 10), (20, 20))

    player_windows = {'inventory_base': InGameWindow(Text('Your inventory', WHITE_RGB, 15, FONT_PATH), (200, 200), (200, 200), DARK_GRAY_RGB)}

    swordsman = Swordsman(player_asset, entities_surface, start_pos=(140, 595), current_item=swordsman_sword)
    NPCs = [swordsman]

    rooms_map = RoomsMap((1, 2))
    make_room(rooms_map.map, (0, 0), DISPLAY.surface, NPCs)
    make_room(rooms_map.map, (1, 0), DISPLAY.surface, [])
    doors = [Door(Tile(TilesAssets().doors['front_door'][0], 'front_door', 0, 0, (350, 0)),
                  Tile(TilesAssets().doors['front_door'][0], 'front_door', 0, 0, (350, 665)),
                  rooms_map.map[0][0], rooms_map.map[1][0],
                  (350, 35), (350, 630))]
    connect_rooms(doors[0])

    for NPC in NPCs:
        NPC.physic.collision.get_collisions_around(rooms_map.get_current_room().collisions_map.map, TILE_SIZE)

    player = Player(player_asset, entities_surface, player_inventory, player_windows, start_pos=BASE_PLAYER_START_POS, current_item=player_sword)
    player.physic.collision.get_collisions_around(rooms_map.get_current_room().collisions_map.map, TILE_SIZE)

    game = Game(DISPLAY, rooms_map, player)
    main_menu = MainMenu(DISPLAY, BACKGROUND_PICTURE, game)
    main = Main(DISPLAY, main_menu, game)

    main.process.run()
