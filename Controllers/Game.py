import pygame as pg
import sys

from Models import Entity
from Models.Asset import TilesAssets
from Utils.TileMap import create_base_tile_map
from Models.Room import Room


class Game:
    def __init__(self, display):
        self.tiles_assets = TilesAssets()
        self.tile_size = (35, 35)

        self.width = 700
        self.height = 700

        self.display = display

        self.base_room_tile_map = create_base_tile_map(self.width, self.height, self.tile_size, self.tiles_assets)
        self.base_room_surface = pg.Surface((self.width, self.height))
        self.base_room = Room(self.width, self.height, self.base_room_tile_map)
        self.base_room.collisions_map.get_map_from_object(self.base_room.room_view.tile_map.tile_map)

        self.player_surface = pg.Surface((self.width, self.height))
        self.player_surface.set_colorkey((0, 0, 0))
        self.player = Entity.Player('Data/Entities/Player/Images/player.png', start_pos=(550., 550.))

        self.is_paused = False

        self.clock = pg.time.Clock()
        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        running = True
        while running:
            self.base_room.room_view.render_tile_map(self.base_room_surface)
            self.base_room_surface.blit(self.player_surface, (0., 0.))
            self.display.surface.blit(self.base_room_surface, self.base_room.room_view.pos)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                old_len = self.player.states_stack.size()
                self.player.states_stack.peek().handle_input(event, self.player.states_stack, None)
                if self.player.states_stack.size() != old_len:
                    self.player.states_stack.peek().handle_input(event, self.player.states_stack, None)
            self.player.states_stack.peek().update(self.base_room)
            self.player.states_stack.peek().draw(self.player_surface)
            self.display.update()
            self.clock.tick(self.fps)
        pg.quit()
        sys.exit()
