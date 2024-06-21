from Views.Entities.Entity import EntityV


class PlayerV(EntityV):
    def __init__(self, windows, paths_asset):
        super().__init__(paths_asset)
        self.windows = windows