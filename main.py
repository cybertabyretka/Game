import pygame as pg

pg.init()
pg.font.init()

from Views.Display import Display

from Models.Main import Main
from Models.Game.Game import Game
from Models.Game.MainMenu import MainMenu
from Models.Asset import WeaponsAssets, PlayerAssets
from Models.RoomsMap import RoomsMap
from Models.Entity.Entity import Swordsman, Player
from Models.Weapon import SwordLike

from Utils.Setting import DISPLAY_WIDTH, DISPLAY_HEIGHT, DISPLAY_NAME, BACKGROUND_PICTURE, DISPLAY


if __name__ == '__main__':
    entities_surface = pg.Surface((DISPLAY_WIDTH, DISPLAY_HEIGHT))

    weapons_assets = WeaponsAssets()
    player_sword = SwordLike('Sword', (35, 35), (35, 35), weapons_assets.sword_asset)
    swordsman_sword = SwordLike('Sword', (35, 35), (35, 35), weapons_assets.sword_asset)

    player_asset = PlayerAssets()

    swordsman = Swordsman(player_asset, entities_surface, start_pos=(140, 595), current_item=swordsman_sword)
    NPCs = [swordsman]

    player = Player(player_asset, entities_surface, start_pos=(560, 560), current_item=player_sword)

    rooms_map = RoomsMap((1, 1))

    game = Game(DISPLAY, rooms_map, NPCs, player)
    main_menu = MainMenu(DISPLAY, BACKGROUND_PICTURE)
    main = Main(DISPLAY, main_menu, game)

    main.process.run()
