from heapq import *

from Utils.CoordinatesConverter import convert_to_int, convert_to_string
from Utils.DistanceCounting import chebyshev_distance


def a_star(start_pos, end_pos, graph):
    path = []
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
            neigh_cost, neigh_node = next_node
            neigh_node = convert_to_int(neigh_node)
            neigh_cost = 1 - neigh_cost
            new_cost = cost_visited[cur_node] + neigh_cost
            if neigh_node not in cost_visited or new_cost < cost_visited[neigh_node]:
                priority = new_cost + chebyshev_distance(neigh_node, end_pos)
                heappush(queue, (priority, neigh_node))
                cost_visited[neigh_node] = new_cost
                visited[neigh_node] = cur_node
    path_head, path_segment = end_pos, end_pos
    while path_segment and path_segment in visited:
        path.insert(0, path_segment)
        path_segment = visited[path_segment]
    return path
