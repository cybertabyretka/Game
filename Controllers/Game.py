import pygame as pg
import sys

from Models import Entity, Weapon
from Models.Asset import TilesAssets, PlayerAssets, WeaponsAssets
from Utils.TileMap import create_base_tile_map
from Models.Room import Room


class Game:
    def __init__(self, display):
        self.tiles_assets = TilesAssets()
        self.tile_size = (35, 35)

        self.width = 700
        self.height = 700

        self.display = display

        self.base_room = Room(create_base_tile_map(self.width, self.height, self.tile_size, self.tiles_assets), pg.Surface((self.width, self.height)))
        self.base_room.collisions_map.get_map_from_object(self.base_room.room_view.tile_map.tile_map)

        self.weapons_assets = WeaponsAssets()
        self.sword = Weapon.SwordLike('Sword', self.weapons_assets.sword_asset)

        self.player_asset = PlayerAssets()
        self.player = Entity.Player(self.player_asset, pg.Surface((self.width, self.height)), start_pos=(550., 550.), current_item=self.sword)

        self.is_paused = False

        self.clock = pg.time.Clock()
        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        running = True
        while running:
            self.base_room.room_view.render_tile_map(self.base_room.room_view.surface)
            self.base_room.room_view.surface.blit(self.player.entity_view.surface, (0., 0.))
            self.display.surface.blit(self.base_room.room_view.surface, (self.base_room.room_view.surface.get_rect().x, self.base_room.room_view.surface.get_rect().y))
            self.player.states_stack.peek().update(self.base_room, self.player.states_stack)
            self.player.states_stack.peek().draw(self.player.entity_view.surface)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                old_len = self.player.states_stack.size()
                self.player.states_stack.peek().handle_input(event, self.player.states_stack)
                if self.player.states_stack.size() != old_len:
                    self.player.states_stack.peek().handle_input(event, self.player.states_stack)
            self.display.update()
            self.clock.tick(self.fps)
        pg.quit()
        sys.exit()
