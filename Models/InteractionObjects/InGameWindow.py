from Views.InteractionObjects.InGameWindow import InGameWindowV


class InGameWindow:
    def __init__(self, name: str, size: tuple[int, int], start_pos: tuple[int, int], colour: tuple[int, int, int]):
        self.view: InGameWindowV = InGameWindowV(colour, name, start_pos, size)
