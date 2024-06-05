def get_damage_and_direction(damage_map, entity_rect):
    damage = 0
    movement = (0, 0)
    for identifier in damage_map:
        damage_rect = damage_map[identifier]
        if entity_rect.colliderect(damage_rect.rect):
            damage += 1
            if damage_rect.direction == 0:
                movement = (0, -entity_rect.width // 2)
            elif damage_rect.direction == 90:
                movement = (entity_rect.width // 2, 0)
            elif damage_rect.direction == 180:
                movement = (0, entity_rect.width // 2)
            else:
                movement = (-entity_rect.width // 2, 0)
    return damage, movement
