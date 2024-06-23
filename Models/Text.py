from Views.Text import TextV


class Text:
    def __init__(self, text: str, text_colour: tuple[int, int, int], font_size: int, font_path: str):
        self.view: TextV = TextV(text, text_colour, font_size, font_path)
