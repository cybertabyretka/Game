import pygame as pg

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile


def draw_projectiles(projectiles: list[BaseProjectile], surface: pg.Surface) -> None:
    for projectile in projectiles:
        projectile.view.draw(projectile.physic.collision.rect.topleft, surface)
