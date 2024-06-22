from Controllers.RoomMap.PathFinding import a_star


class Mind:
    def __init__(self):
        self.way = None

    def search_way_in_graph(self, start_pos, end_pos, graph):
        self.way = a_star(start_pos, end_pos, graph)