from Views.Entities.Entity import EntityV

from Models.InteractionObjects.InGameWindow import InGameWindow


class PlayerV(EntityV):
    def __init__(self, windows: dict[str, InGameWindow], paths_asset: dict[str, str]):
        super().__init__(paths_asset)
        self.windows: dict[str, InGameWindow] = windows
