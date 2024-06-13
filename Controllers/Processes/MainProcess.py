import pygame as pg

from Utils.Settings.DataStructures.Stack import Stack


class MainProcess:
    def __init__(self, main_menu):
        self.processes_stack = Stack(main_menu)
        self.is_running = False
        self.clock = pg.time.Clock()
        self.speed = 1.0
        self.fps = 60 * self.speed
        self.delta_time = 0.016

    def run(self):
        self.is_running = True
        while self.is_running:
            self.processes_stack.peek().process.do(self.processes_stack, self)
            self.clock.tick(self.fps)
