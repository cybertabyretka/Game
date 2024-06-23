import pygame as pg

from Constants.Colours import GREEN_RGB, RED_RGB


class HealthBarV:
    @staticmethod
    def draw(surface: pg.Surface, entity_rect: pg.Rect, health: int, max_health: int) -> None:
        pos = [entity_rect.x - ((max_health - entity_rect.width) // 2), entity_rect.y + entity_rect.height + 1]
        for i in range(max_health):
            if i < health:
                pg.draw.rect(surface, GREEN_RGB, (pos[0], pos[1], 1, 3))
            else:
                pg.draw.rect(surface, RED_RGB, (pos[0], pos[1], 1, 3))
            pos[0] += 1