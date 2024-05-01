import pygame as pg
import sys

from Models import Entities
from Controllers import EntityPhysics


class Game:
    def __init__(self, display):
        self.player = Entities.Player()
        self.player_physic = EntityPhysics.PlayerPhysicsEntity(self.player)
        self.player_img = pg.image.load('Data/Entities/Player/Images/player.png')

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
            self.display.screen.fill((125, 125, 125))
            self.player_physic.update_pos()
            self.display.draw_img(self.player_img, (self.player.collision[0], self.player.collision[1]))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player.velocity[1] -= self.player.max_velocity
                    if event.key == pg.K_s:
                        self.player.velocity[1] += self.player.max_velocity
                    if event.key == pg.K_a:
                        self.player.velocity[0] -= self.player.max_velocity
                    if event.key == pg.K_d:
                        self.player.velocity[0] += self.player.max_velocity
                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.player.velocity[1] += self.player.max_velocity
                    if event.key == pg.K_s:
                        self.player.velocity[1] -= self.player.max_velocity
                    if event.key == pg.K_a:
                        self.player.velocity[0] += self.player.max_velocity
                    if event.key == pg.K_d:
                        self.player.velocity[0] -= self.player.max_velocity
            self.display.update()
            self.clock.tick(self.fps)
        pg.quit()
        sys.exit()
