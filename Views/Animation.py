import pygame as pg


class Animation:
    def __init__(self, images: list[pg.Surface], image_duration: int, loop: bool):
        self.images: list[pg.Surface] = images
        self.image_duration: int = image_duration
        self.loop: bool = loop
        self.done: bool = False
        self.frame: int = 0
        self.pos: tuple[int, int] = (0, 0)

    def copy(self):
        return Animation(self.images, self.image_duration, self.loop)

    def get_image(self) -> pg.Surface:
        image = self.images[int(self.frame / self.image_duration)]
        return image

    def update(self) -> None:
        if self.loop:
            self.frame = (self.frame + 1) % (self.image_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.image_duration * len(self.images) - 1)
            if self.frame >= self.image_duration * len(self.images) - 1:
                self.done = True

    def draw(self, surface: pg.Surface) -> None:
        surface.blit(self.get_image(), self.pos)
        self.update()
