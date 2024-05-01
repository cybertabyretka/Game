from Maps import TileMap
from Utils.Maps import create_base_map


tile_map_width = tile_map_height = 700
tile_size = 35
tile_map = TileMap(tile_map_width, tile_map_height, tile_size)
create_base_map(tile_map)
print(tile_map.tile_map)
