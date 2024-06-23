import pygame as pg

from DataStructures.Stack import Stack


class MainProcess:
    def __init__(self):
        self.processes_stack: Stack = Stack()
        self.is_running: bool = False
        self.clock: pg.time.Clock = pg.time.Clock()
        self.speed: float = 1.0
        self.fps: float = 60 * self.speed
        self.delta_time: float = 0.016

    def run(self) -> None:
        self.is_running = True
        while self.is_running:
            self.processes_stack.peek().process.do(self.processes_stack, self)
            self.clock.tick(self.fps)
