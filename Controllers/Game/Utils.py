def check_buttons_collisions(mouse_pos, state):
    for button in state.buttons:
        if button.view.rect.collidepoint(mouse_pos):
            if state.selected_button is not None and state.selected_button != button:
                state.selected_button.view.selected = False
            button.view.selected = True
            state.selected_button = button
            return
    if state.selected_button is not None:
        state.selected_button.view.selected = False
        state.selected_button = None