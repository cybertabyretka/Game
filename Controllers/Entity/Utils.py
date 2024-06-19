def get_damage_and_movement(damage_map, entity_rect):
    types = {}
    movement = (0, 0)
    for identifier in damage_map:
        damage_rect = damage_map[identifier]
        if entity_rect.colliderect(damage_rect.rect):
            for damage_type in damage_rect.damage_types:
                if damage_type not in types:
                    types[damage_type] = [damage_rect.copy()]
                else:
                    types[damage_type].append(damage_rect.copy())
                if damage_rect.direction == 0:
                    movement = (0, -entity_rect.width // 2)
                elif damage_rect.direction == 90:
                    movement = (entity_rect.width // 2, 0)
                elif damage_rect.direction == 180:
                    movement = (0, entity_rect.width // 2)
                else:
                    movement = (-entity_rect.width // 2, 0)
    return types, movement


def check_damage_for_entity(entity, damage_map, after_punch_state):
    damage, movement = get_damage_and_movement(damage_map, entity.physic.collision.rect)
    if damage:
        entity.states_stack.push(after_punch_state(entity, movement, damage))
        return True
    return False


def check_damage_for_entity_with_ready_damage_and_movement(entity, damage, movement, after_punch_state):
    if damage:
        entity.states_stack.push(after_punch_state(entity, movement, damage))
        return True
    return False