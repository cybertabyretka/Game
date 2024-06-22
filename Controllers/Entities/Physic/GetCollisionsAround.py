from BaseVariables.TileMapOffsets import NEIGHBOUR_OFFSETS


def get_collisions_around(rect, tile_size, collisions_map, collisions_around):
    tile_loc = ((rect.x + (rect.width // 2)) // tile_size[0], (rect.y + (rect.height // 2)) // tile_size[1])
    for offset_name in NEIGHBOUR_OFFSETS:
        check_lock = str((tile_loc[0] + NEIGHBOUR_OFFSETS[offset_name][0]) * tile_size[0]) + ';' + str((tile_loc[1] + NEIGHBOUR_OFFSETS[offset_name][1]) * tile_size[1])
        if check_lock in collisions_map:
            collisions_around[offset_name] = collisions_map[check_lock]