import pygame as pg

from Utils.Draw.DrawText import draw_text

from BaseVariables.Paths import FONT_PATH

from Constants.Colours import WHITE_RGB

from Models.InteractionObjects.Button import Button
from Models.Save import Save


def draw_save_selection_state(surface: pg.Surface, buttons: list[Button], auto_saves: list[Save], saves: list[Save], background_colour: tuple[int, int, int]):
    surface.fill(background_colour)
    ratio_of_display_length_to_number_of_saves = surface.get_width() // len(auto_saves)
    line_start_pos = [ratio_of_display_length_to_number_of_saves - 5, 20]
    line_end_pos = [ratio_of_display_length_to_number_of_saves - 5, 200]
    date_start_pos = [0, 50]
    for button in buttons:
        button.view.draw(surface)
    draw_text(surface, auto_saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
    for i in range(2):
        if not i:
            saves_to_draw = auto_saves
        else:
            saves_to_draw = saves
        for j in range(1, len(saves_to_draw)):
            pg.draw.line(surface, WHITE_RGB, line_start_pos, line_end_pos, 1)
            date_start_pos[0] += ratio_of_display_length_to_number_of_saves
            draw_text(surface, saves_to_draw[j].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
            line_start_pos[0] += ratio_of_display_length_to_number_of_saves
            line_end_pos[0] += ratio_of_display_length_to_number_of_saves
            if j == len(saves_to_draw) - 1 and not i:
                line_start_pos = [ratio_of_display_length_to_number_of_saves - 5, 210]
                line_end_pos = [ratio_of_display_length_to_number_of_saves - 5, 390]
                date_start_pos = [0, 250]
                draw_text(surface, saves[0].save_time, WHITE_RGB, 15, FONT_PATH, date_start_pos)
