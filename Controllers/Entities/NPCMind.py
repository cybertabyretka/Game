from Controllers.RoomMap.PathFinding import a_star


class Mind:
    def __init__(self):
        self.way: list[tuple[int, int]] | None = None

    def search_way_in_graph(self, start_pos: tuple[int, int], end_pos: tuple[int, int], graph: dict[str, list[tuple[int, str]]]) -> None:
        self.way = a_star(start_pos, end_pos, graph)
