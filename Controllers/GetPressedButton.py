def get_pressed_button(buttons, mouse_clck_pos):
    for button in buttons:
        if button.view.rect.collidepoint(mouse_clck_pos):
            return button
    return None