from Views.Text import TextV


class Text:
    def __init__(self, text, text_colour, font_size, font_path):
        self.view = TextV(text, text_colour, font_size, font_path)