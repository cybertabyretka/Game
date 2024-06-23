from collections.abc import Iterable


def manhattan_distance(start_pos: Iterable[int], end_pos: Iterable[int]) -> int:
    return abs(start_pos[0] - end_pos[0]) + abs(start_pos[1] - end_pos[1])


def chebyshev_distance(start_pos: Iterable[int], end_pos: Iterable[int]) -> int:
    return max(abs(start_pos[0] - end_pos[0]), abs(start_pos[1] - end_pos[1]))
