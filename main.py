import sys
import pygame as pg
pg.init()


class Player:
    def __init__(self):
        self.collision = pg.rect
        self.x_movement = [False, False]
        self.y_movement = [False, False]


class Display:
    def __init__(self, width, height, name):
        self.width = width
        self.height = height
        self.display = pg.display
        self.screen = self.display.set_mode((width, height))
        self.display.set_caption(name)
        self.name = name

    def update(self):
        self.display.flip()


class Game:
    def __init__(self, display):
        self.player = Player()
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


if __name__ == '__main__':
    width, height, name = 700, 700, 'Dungeon'
    game = Game(Display(width, height, name))
    game.run()
