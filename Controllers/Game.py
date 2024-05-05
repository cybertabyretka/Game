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
        self.player = Entity.Player(pg.image.load('Data/Entities/Player/Images/player.png'), start_pos=(550., 550.))

        self.is_paused = False

        self.clock = pg.time.Clock()
        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        running = True
        while running:
            self.player.physic.collision.get_collisions_around(self.base_room.collisions_map.map, self.base_room.room_view.tile_size)
            self.player.physic.collision.update(self.player.physic.velocity)
            self.base_room.room_view.render_tile_map(self.base_room_surface)
            self.player.entity_view.clear_surface(self.player_surface)
            self.player.entity_view.render(self.player_surface, (self.player.physic.collision.rect.x, self.player.physic.collision.rect.y))
            self.base_room_surface.blit(self.player_surface, (0., 0.))
            self.display.surface.blit(self.base_room_surface, self.base_room.room_view.pos)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player.physic.velocity[1] -= self.player.physic.max_velocity
                    if event.key == pg.K_s:
                        self.player.physic.velocity[1] += self.player.physic.max_velocity
                    if event.key == pg.K_a:
                        self.player.physic.velocity[0] -= self.player.physic.max_velocity
                    if event.key == pg.K_d:
                        self.player.physic.velocity[0] += self.player.physic.max_velocity
                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.player.physic.velocity[1] += self.player.physic.max_velocity
                    if event.key == pg.K_s:
                        self.player.physic.velocity[1] -= self.player.physic.max_velocity
                    if event.key == pg.K_a:
                        self.player.physic.velocity[0] += self.player.physic.max_velocity
                    if event.key == pg.K_d:
                        self.player.physic.velocity[0] -= self.player.physic.max_velocity
            self.display.update()
            self.clock.tick(self.fps)
        pg.quit()
        sys.exit()
