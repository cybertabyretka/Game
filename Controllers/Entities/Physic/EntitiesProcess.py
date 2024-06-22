def entities_process(movement, entity_rect, self_rect):
    if movement[0] > 0 and (entity_rect.x - self_rect.topright[0]) >= 0 and abs(self_rect.y - entity_rect.y) <= self_rect.height:
        movement[0] = min(movement[0], entity_rect.x - self_rect.topright[0])
    if movement[0] < 0 and (entity_rect.topright[0] - self_rect.x) <= 0 and abs(self_rect.y - entity_rect.y) <= self_rect.height:
        movement[0] = max(movement[0], entity_rect.topright[0] - self_rect.x)
    if movement[1] > 0 and (entity_rect.y - self_rect.bottomleft[1]) >= 0 and abs(self_rect.x - entity_rect.x) <= self_rect.width:
        movement[1] = min(movement[1], entity_rect.y - self_rect.bottomleft[1])
    if movement[1] < 0 and (entity_rect.bottomleft[1] - self_rect.y) <= 0 and abs(self_rect.x - entity_rect.x) <= self_rect.width:
        movement[1] = max(movement[1], entity_rect.bottomleft[1] - self_rect.y)