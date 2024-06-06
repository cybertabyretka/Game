from Views.Button import ButtonV


class Button:
    def __init__(self, rect, rect_colour, text):
        self.view = ButtonV(rect, rect_colour, text)