import pygame as pg
from Utils.Setting import GREEN_RGB, RED_RGB


class HealthBarV:
    @staticmethod
    def draw(surface, entity_rect, health, max_health):
        pos = [entity_rect.x - ((max_health - entity_rect.width) // 2), entity_rect.y + entity_rect.height + 1]
        for i in range(max_health):
            if i < health:
                pg.draw.rect(surface, GREEN_RGB, (pos[0], pos[1], 1, 3))
            else:
                pg.draw.rect(surface, RED_RGB, (pos[0], pos[1], 1, 3))
            pos[0] += 1


def render_health_bars(entities, surface):
    for entity in entities:
        entity.health.view.draw(surface, entity.physic.collision.rect, entity.health.health, entity.health.max_health)