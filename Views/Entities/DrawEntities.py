import pygame as pg

from Models.Entities.NPCs.BaseNPC import NPC
from Models.Entities.Player import Player


def draw_entities(NPCs: list[NPC], player: Player, surface: pg.Surface, base_colour: tuple[int, int, int] = (0, 0, 0)) -> None:
    surface.set_colorkey(base_colour)
    surface.fill(base_colour)
    for NPC in NPCs:
        NPC.states_stack.peek().draw(surface)
    player.states_stack.peek().draw(surface)
