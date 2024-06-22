import pygame as pg

from Views.Text.DrawText import draw_text

from BaseVariables.Paths import FONT_PATH

from Constants.Colours import WHITE_RGB


def draw_save_selection_state(surface, buttons, auto_saves, saves, background_colour):
    surface.fill(background_colour)
    ratio_of_display_length_to_number_of_saves = surface.get_width // len(auto_saves)
    line_start_pos = [ratio_of_display_length_to_number_of_saves - 5, 20]
    line_end_pos = [ratio_of_display_length_to_number_of_saves - 5, 200]
    date_start_pos = [0, 50]
    for button in buttons:
        button.view.draw(surface)
    draw_text(surface, self.game.auto_saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
    for auto_save in self.game.auto_saves[1:]:
        pg.draw.line(surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
        date_start_pos[0] += ratio_of_display_length_to_number_of_saves
        draw_text(surface, auto_save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        line_start_pos[0] += ratio_of_display_length_to_number_of_saves
        line_end_pos[0] += ratio_of_display_length_to_number_of_saves
    line_start_pos = [ratio_of_display_length_to_number_of_saves - 5, 210]
    line_end_pos = [ratio_of_display_length_to_number_of_saves - 5, 390]
    date_start_pos = [0, 250]
    draw_text(surface, saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
    for save in self.game.saves[1:]:
        pg.draw.line(self.game.view.display.surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
        date_start_pos[0] += ratio_of_display_length_to_number_of_saves
        draw_text(surface, save.save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
        line_start_pos[0] += ratio_of_display_length_to_number_of_saves
        line_end_pos[0] += ratio_of_display_length_to_number_of_saves