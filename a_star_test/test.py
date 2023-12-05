import given_code.min_heap2 as min_heap
from given_code.final_project_part1 import *
from given_code.min_heap2 import MinHeap, Element
from math import sqrt


def dijkstra(G, source, dest):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    Q = min_heap.MinHeap([])
    nodes = list(G.adj.keys())
    num_nodes = 0
    # Initialize priority queue/heap and distances
    for node in nodes:
        Q.insert(min_heap.Element(node, float("inf")))
        dist[node] = float("inf")
    Q.decrease_key(source, 0)

    # Meat of the algorithm
    while not Q.is_empty():
        current_element = Q.extract_min()
        num_nodes += 1
        current_node = current_element.value
        dist[current_node] = current_element.key
        if current_node == dest:
            break
        for neighbour in G.adj[current_node]:
            if dist[current_node] + G.w(current_node, neighbour) < dist[neighbour]:
                Q.decrease_key(neighbour, dist[current_node] + G.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + G.w(current_node, neighbour)
                pred[neighbour] = current_node
    return num_nodes, dist[dest]


def a_star(G: DirectedWeightedGraph, s: int, d: int, h: dict[int, float]):
    g_distances = {}
    predecessors = {}
    f_scores = {}
    num_nodes = 0
    # Keep track of all the nodes in the priority queue. This is to make sure that nodes that were popped
    # previously from the heap but have gotten better scores from the heuristics are reconsidered
    in_pq: dict[int, bool] = {}
    pq = MinHeap([])
    for node in G.adj.keys():
        g_distances[node] = float('inf')
        f_scores[node] = float('inf')
        pq.insert(Element(node, f_scores[node]))
        in_pq[node] = True

    g_distances[s] = 0
    f_scores[s] = g_distances[s] + h[s]
    pq.decrease_key(s, f_scores[s])
    while not pq.is_empty():
        cur_elem = pq.extract_min()
        num_nodes += 1
        cur_node, cur_score = cur_elem.value, cur_elem.key
        in_pq[cur_node] = False
        if cur_node == d:
            break
        for nbr in G.adj[cur_node]:
            new_dist = g_distances[cur_node] + G.w(cur_node, nbr)
            if new_dist < g_distances[nbr]:
                predecessors[nbr] = cur_node
                g_distances[nbr] = new_dist
                f_scores[nbr] = new_dist + h[nbr]
                # If the neighbour is in the pq currently then decrease the key
                # Otherwise re-insert it (this is for the edge case that the heuristic might overshoot but
                # isn't incorrect)
                if in_pq[nbr]:
                    pq.decrease_key(nbr, f_scores[nbr])
                else:
                    pq.insert(Element(nbr, f_scores[nbr]))

    return num_nodes, g_distances[d]


def create_test_graph(rows, columns):
    G = DirectedWeightedGraph()

    for i in range(rows):
        for j in range(columns):
            G.add_node((i, j))

    for i in range(rows):
        for j in range(columns):
            curr_node = (i, j)

            # add edge between current node and right neighbour
            if j < columns - 1:
                right_node = (i, j + 1)
                G.add_edge(curr_node, right_node, 1)
                G.add_edge(right_node, curr_node, 1)
            # add edge between current node and bottom neighbour
            if i < rows - 1:
                bottom_node = (i + 1, j)
                G.add_edge(curr_node, bottom_node, 1)
                G.add_edge(bottom_node, curr_node, 1)
            # add edge between current node and bottom-right neighbour
            if i < rows - 1 and j < columns - 1:
                bt_right_node = (i + 1, j + 1)
                G.add_edge(curr_node, bt_right_node, sqrt(2))
                G.add_edge(bt_right_node, curr_node, sqrt(2))
            # add edge between current node and top-right neighbour
            if i > 0 and j < columns - 1:
                tp_right_node = (i - 1, j + 1)
                G.add_edge(curr_node, tp_right_node, sqrt(2))
                G.add_edge(tp_right_node, curr_node, sqrt(2))

    return G


def heuristic(G: DirectedWeightedGraph, Destination: tuple[int, int]) -> dict[int, float]:
    heuristic_distances = {}

    for node in G.adj.keys():
        x1, y1 = node
        x2, y2 = Destination
        dist = sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        heuristic_distances[node] = dist
    return heuristic_distances


g = create_test_graph(11, 11)
nodes = list(g.adj.keys())
source = nodes[60]
dest = nodes[120]
h = heuristic(g, dest)
print(dijkstra(g, source, dest))
print(a_star(g, source, dest, h))
