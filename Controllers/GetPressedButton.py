from Models.InteractionObjects.Button import Button


def get_pressed_button(buttons: list[Button], mouse_clck_pos: tuple[int, int]) -> Button | None:
    for button in buttons:
        if button.view.rect.collidepoint(mouse_clck_pos):
            return button
    return None