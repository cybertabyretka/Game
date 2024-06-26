from BaseVariables.TileMapOffsets import NEIGHBOUR_OFFSETS

from Models.Room.Door import Door

from Controllers.RoomMap.TilePhysic import TileCollision
from Controllers.Weapons.AttackPhysic import AttackPhysic

from Constants.Directions import *

from Models.Items.Weapons.Projectiles.BaseProjectile import BaseProjectile
from Models.Room.Tile import Tile


class CollisionsMap:
    def __init__(self):
        self.doors: list[Door] = []
        self.map: dict[str, TileCollision] = {}
        self.graph: dict[str, list[tuple[int, str]]] = {}
        self.damage_map: dict[int, AttackPhysic] = {}
        self.movable_damage_map: list[BaseProjectile] = []

    def get_map_from_object(self, tile_map: dict[str, Tile]) -> None:
        for loc in tile_map:
            self.map[loc] = tile_map[loc].collision

    def get_graph(self) -> None:
        for loc in self.map:
            straight_directions_cross_ability = {UP: 1, LEFT: 1, RIGHT: 1, DOWN: 1}
            current_tile = self.map[loc]
            if current_tile.cross_ability != 0:
                loc_int = loc.split(';')
                loc_int = [int(loc_int[0]) // current_tile.rect.width, int(loc_int[1]) // current_tile.rect.height]
                for offset in NEIGHBOUR_OFFSETS:
                    cross_ability = 0
                    check_loc = str((loc_int[0] + NEIGHBOUR_OFFSETS[offset][0]) * current_tile.rect.width) + ';' + str((loc_int[1] + NEIGHBOUR_OFFSETS[offset][1]) * current_tile.rect.height)
                    if check_loc in self.map and check_loc != loc:
                        if self.map[check_loc].cross_ability != 0:
                            if offset == LEFT_UP:
                                if straight_directions_cross_ability[LEFT] != 0 and straight_directions_cross_ability[UP] != 0:
                                    cross_ability = self.map[check_loc].cross_ability * 1.5
                            elif offset == RIGHT_UP:
                                if straight_directions_cross_ability[RIGHT] != 0 and straight_directions_cross_ability[UP] != 0:
                                    cross_ability = self.map[check_loc].cross_ability * 1.5
                            elif offset == LEFT_DOWN:
                                if straight_directions_cross_ability[LEFT] != 0 and straight_directions_cross_ability[DOWN] != 0:
                                    cross_ability = self.map[check_loc].cross_ability * 1.5
                            elif offset == RIGHT_DOWN:
                                if straight_directions_cross_ability[RIGHT] != 0 and straight_directions_cross_ability[DOWN] != 0:
                                    cross_ability = self.map[check_loc].cross_ability * 1.5
                            else:
                                cross_ability = self.map[check_loc].cross_ability
                        else:
                            if offset in straight_directions_cross_ability:
                                straight_directions_cross_ability[offset] = self.map[check_loc].cross_ability
                    if cross_ability:
                        if loc in self.graph:
                            self.graph[loc].append((cross_ability, check_loc))
                        else:
                            self.graph[loc] = [(cross_ability, check_loc)]

    def add_damage(self, damage: AttackPhysic, identifier: int) -> None:
        self.damage_map[identifier] = damage

    def remove_damage(self, identifier: int) -> None:
        if identifier in self.damage_map:
            del self.damage_map[identifier]