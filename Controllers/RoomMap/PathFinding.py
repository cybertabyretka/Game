from heapq import *

from Utils.CoordinatesConverter import convert_to_int, convert_to_string
from Utils.DistanceCounting import chebyshev_distance


def a_star(start_pos: tuple[int, int], end_pos: tuple[int, int], graph: dict[str, list[tuple[int, str]]]) -> list[tuple[int, int]]:
    queue = []
    heappush(queue, (0, start_pos))
    cost_visited = {start_pos: 0}
    visited = {start_pos: None}
    while queue:
        cur_cost, cur_node = heappop(queue)
        if cur_node == end_pos:
            break
        next_nodes = graph[convert_to_string(cur_node)]
        for next_node in next_nodes:
            neighbour_cost, neighbour_node = next_node
            neighbour_node = convert_to_int(neighbour_node)
            new_cost = cost_visited[cur_node] + neighbour_cost
            if neighbour_node not in cost_visited or new_cost < cost_visited[neighbour_node]:
                priority = new_cost + chebyshev_distance(neighbour_node, end_pos)
                heappush(queue, (priority, neighbour_node))
                cost_visited[neighbour_node] = new_cost
                visited[neighbour_node] = cur_node
    path_head, path_segment = end_pos, end_pos
    path = []
    while path_segment is not None and path_segment in visited:
        path.insert(0, path_segment)
        path_segment = visited[path_segment]
    return path
