from Utils.Setting import NEIGHBOUR_OFFSETS


class CollisionsMap:
    def __init__(self):
        self.map = {}
        self.graph = {}

    def get_map_from_object(self, tile_map):
        for loc in tile_map:
            tile = tile_map[loc]
            self.map[loc] = tile.collision

    def get_graph(self):
        for loc in self.map:
            straight_directions_cross_ability = {'up': 1, 'left': 1, 'right': 1, 'down': 1}
            current_tile = self.map[loc]
            if current_tile.cross_ability != 0:
                loc_int = loc.split(';')
                loc_int = [int(loc_int[0]) // current_tile.rect.width, int(loc_int[1]) // current_tile.rect.height]
                for offset in NEIGHBOUR_OFFSETS:
                    check_loc_is_right = False
                    check_loc = str((loc_int[0] + NEIGHBOUR_OFFSETS[offset][0]) * current_tile.rect.width) + ';' + str((loc_int[1] + NEIGHBOUR_OFFSETS[offset][1]) * current_tile.rect.height)
                    if check_loc in self.map and check_loc != loc:
                        if self.map[check_loc].cross_ability != 0:
                            if offset == 'left_up':
                                if straight_directions_cross_ability['left'] != 0 and straight_directions_cross_ability['up'] != 0:
                                    check_loc_is_right = True
                            elif offset == 'right_up':
                                if straight_directions_cross_ability['right'] != 0 and straight_directions_cross_ability['up'] != 0:
                                    check_loc_is_right = True
                            elif offset == 'left_down':
                                if straight_directions_cross_ability['left'] != 0 and straight_directions_cross_ability['down'] != 0:
                                    check_loc_is_right = True
                            elif offset == 'right_down':
                                if straight_directions_cross_ability['right'] != 0 and straight_directions_cross_ability['down'] != 0:
                                    check_loc_is_right = True
                            else:
                                check_loc_is_right = True
                        else:
                            if offset in straight_directions_cross_ability:
                                straight_directions_cross_ability[offset] = self.map[check_loc].cross_ability
                    if check_loc_is_right:
                        if loc in self.graph:
                            self.graph[loc].append(check_loc)
                        else:
                            self.graph[loc] = [check_loc]
