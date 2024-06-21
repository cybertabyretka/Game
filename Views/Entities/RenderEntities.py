def render_entities(NPCs, player, surface, base_colour=(0, 0, 0)):
    surface.set_colorkey(base_colour)
    surface.fill(base_colour)
    for NPC in NPCs:
        NPC.states_stack.peek().draw(surface)
    player.states_stack.peek().draw(surface)