import pygame as pg
import sys

from Views.Entity import render_entities
from Models import Entity, Weapon
from Models.Asset import TilesAssets, PlayerAssets, WeaponsAssets
from Utils.TileMap import create_base_tile_map
from Models.Room import Room


class Game:
    def __init__(self, display):
        self.tiles_assets = TilesAssets()
        self.tile_size = (35, 35)

        self.width = 700
        self.height = 700

        self.display = display

        self.base_room = Room(create_base_tile_map(self.width, self.height, self.tile_size, self.tiles_assets), pg.Surface((self.width, self.height)))
        self.base_room.collisions_map.get_map_from_object(self.base_room.room_view.tile_map.tile_map)
        self.base_room.collisions_map.get_graph()

        self.entities_surface = pg.Surface((self.width, self.height))

        self.weapons_assets = WeaponsAssets()
        self.sword = Weapon.SwordLike('Sword', self.weapons_assets.sword_asset)

        self.player_asset = PlayerAssets()

        self.swordsman = Entity.Swordsman(self.player_asset, self.entities_surface, start_pos=(140., 140.), current_item=self.sword)
        self.swordsman.physic.collision.get_collisions_around(self.base_room.collisions_map.map, 35)

        self.player = Entity.Player(self.player_asset, self.entities_surface, start_pos=(560., 560.), current_item=self.sword)
        self.player.physic.collision.get_collisions_around(self.base_room.collisions_map.map, 35)

        self.entities = [self.swordsman, self.player]

        self.is_paused = False

        self.clock = pg.time.Clock()
        self.game_speed = 1.0
        self.fps = 60 * self.game_speed
        self.delta_time = 0.016

    def run(self):
        running = True
        while running:
            self.base_room.room_view.render_tile_map(self.base_room.room_view.surface)
            self.base_room.room_view.surface.blit(self.player.entity_view.surface, (0., 0.))
            self.display.surface.blit(self.base_room.room_view.surface, (self.base_room.room_view.surface.get_rect().x, self.base_room.room_view.surface.get_rect().y))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False
                old_len = self.player.states_stack.size()
                self.player.states_stack.peek().handle_input(event, self.player.states_stack)
                if self.player.states_stack.size() != old_len:
                    self.player.states_stack.peek().handle_input(event, self.player.states_stack)
            self.player.states_stack.peek().update(self.base_room, self.player.states_stack)
            render_entities(self.entities, self.entities_surface)
            self.swordsman.mind.search_way_in_graph(f'{self.swordsman.physic.collision.collisions_around["center"].rect.x};{self.swordsman.physic.collision.collisions_around["center"].rect.y}', f'{self.player.physic.collision.collisions_around["center"].rect.x};{self.player.physic.collision.collisions_around["center"].rect.y}', self.base_room.collisions_map.graph)
            for coord in self.swordsman.mind.way:
                if self.swordsman.mind.way[coord] is not None:
                    coord1_int = coord.split(';')
                    coord1_int = (int(coord1_int[0]) + 17, int(coord1_int[1]) + 17)
                    coord2_int = self.swordsman.mind.way[coord].split(';')
                    coord2_int = (int(coord2_int[0]) + 17, int(coord2_int[1]) + 17)
                    pg.draw.line(self.entities_surface, (255, 0, 0), coord1_int, coord2_int)
            self.display.update()
            self.clock.tick(self.fps)
        pg.quit()
        sys.exit()
