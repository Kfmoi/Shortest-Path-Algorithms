from graph import HeuristicGraph, WeightedGraph
from short_path_finder import ShortPathFinder
from spalgorithm import Dijkstra, Bellman_Ford, A_Star
from math import sqrt

if __name__ == "__main__":
    graph = WeightedGraph()
    for i in range(11):
        for j in range(11):
            graph.add_node((i,j))

    for i in range(11):
        for j in range(11):
            curr_node = (i, j)

            # add edge between current node and right neighbour
            if j < 11 - 1:
                right_node = (i, j + 1)
                graph.add_edge(curr_node, right_node, 1)
                graph.add_edge(right_node, curr_node, 1)
            # add edge between current node and bottom neighbour
            if i < 11 - 1:
                bottom_node = (i + 1, j)
                graph.add_edge(curr_node, bottom_node, 1)
                graph.add_edge(bottom_node, curr_node, 1)
            # add edge between current node and bottom-right neighbour
            if i < 11 - 1 and j < 11 - 1:
                bt_right_node = (i + 1, j + 1)
                graph.add_edge(curr_node, bt_right_node, sqrt(2))
                graph.add_edge(bt_right_node, curr_node, sqrt(2))
            # add edge between current node and top-right neighbour
            if i > 0 and j < 11 - 1:
                tp_right_node = (i - 1, j + 1)
                graph.add_edge(curr_node, tp_right_node, sqrt(2))
                graph.add_edge(tp_right_node, curr_node, sqrt(2))

    algorithm = Dijkstra()
    path_finder = ShortPathFinder()
    path_finder.set_graph(graph)
    path_finder.set_algorithm(algorithm)
    nodes = list(graph.adj.keys())
    source = nodes[60]
    dest = nodes[120]
    short_path = path_finder.calc_short_path(source,dest)
    print(short_path)