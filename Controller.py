import pygame as pg
import sys

import Model


class Game:
    def __init__(self, display):
        self.player = Model.Player()
        self.img = pg.image.load('Data/Entities/Player/Images/player.png')
        self.player_pos = [100, 100]

        self.display = display

        self.is_paused = False

        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        clock = pg.time.Clock()
        self.display.update()
        running = True
        while running:
            self.display.screen.fill((125, 125, 125))
            self.player_pos[1] += self.player.y_movement[1] - self.player.y_movement[0]
            self.player_pos[0] += self.player.x_movement[1] - self.player.x_movement[0]
            self.display.screen.blit(self.img, self.player_pos)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_w:
                        self.player.y_movement[0] = True
                    if event.key == pg.K_s:
                        self.player.y_movement[1] = True
                    if event.key == pg.K_a:
                        self.player.x_movement[0] = True
                    if event.key == pg.K_d:
                        self.player.x_movement[1] = True
                if event.type == pg.KEYUP:
                    if event.key == pg.K_w:
                        self.player.y_movement[0] = False
                    if event.key == pg.K_s:
                        self.player.y_movement[1] = False
                    if event.key == pg.K_a:
                        self.player.x_movement[0] = False
                    if event.key == pg.K_d:
                        self.player.x_movement[1] = False
            self.display.update()
            clock.tick(self.fps)
        pg.quit()
        sys.exit()
