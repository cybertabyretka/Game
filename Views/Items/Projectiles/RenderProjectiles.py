def render_projectiles(projectiles, surface):
    for projectile in projectiles:
        projectile.view.draw(projectile.physic.collision.rect.topleft, surface)