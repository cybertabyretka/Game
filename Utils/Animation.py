class Animation:
    def __init__(self, images, image_duration, loop, game_fps):
        self.images = images
        self.image_duration = image_duration
        self.loop = loop
        self.done = False
        self.frame = 0
        self.game_fps = game_fps
        self.duration = (len(images) * image_duration) / game_fps

    def copy(self):
        return Animation(self.images, self.image_duration, self.loop, self.game_fps)

    def get_image(self):
        return self.images[int(self.frame / self.image_duration)]

    def update(self):
        if self.loop:
            self.frame = (self.frame + 1) % (self.image_duration * len(self.images))
        else:
            self.frame = min(self.frame + 1, self.image_duration * len(self.images) - 1)
            if self.frame >= self.image_duration * len(self.images) - 1:
                self.done = True

    def render(self, pos, surface):
