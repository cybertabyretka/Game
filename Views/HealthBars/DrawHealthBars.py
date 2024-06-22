def draw_health_bars(NPCs, player, surface):
    for NPC in NPCs:
        if NPC.health.health > 0:
            NPC.health.view.draw(surface, NPC.physic.collision.rect, NPC.health.health, NPC.health.max_health)
    player.health.view.draw(surface, player.physic.collision.rect, player.health.health, player.health.max_health)