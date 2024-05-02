import pygame as pg
import sys

from Models import Entities
from Models.Environment import TilesAssets
from Utils.Maps import create_base_map


class Game:
    def __init__(self, display):
        self.tiles_assets = TilesAssets()
        self.tile_size = (35, 35)

        self.map_width = 700
        self.map_height = 700
        self.base_tile_map = create_base_map(self.map_width, self.map_height, self.tile_size, self.tiles_assets)

        self.player = Entities.Player(pg.image.load('Data/Entities/Player/Images/player.png'))

        self.display = display

        self.is_paused = False

        self.clock = pg.time.Clock()
        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        self.display.update()
        running = True
        while running:
            self.base_tile_map.render(self.display.surface)
            self.player.physic.update_collision()
            self.display.draw_img(self.player.image, (self.player.physic.collision.rect[0], self.player.physic.collision.rect[1]))
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
