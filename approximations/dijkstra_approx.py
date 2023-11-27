from given_code.final_project_part1 import DirectedWeightedGraph
from given_code.min_heap2 import MinHeap, Element


def dijkstra_approx(G: DirectedWeightedGraph, source: int, k: int) -> dict[int, float]:
    # If the node is the source node, it will have a distance of 0. If a node is unreachable, it will have distance of
    # `inf`.
    distances = {}
    relaxations = {}
    pq = MinHeap([])
    for node in G.adj.keys():
        pq.insert(Element(node, float("inf")))
        distances[node] = float("inf")
        relaxations[node] = 0

    # Update source node
    distances[source] = 0
    pq.decrease_key(source, 0)
    # Run Dijkstra's with k-approximation
    while not pq.is_empty():
        cur_elem = pq.extract_min()
        cur_node, cur_dist = cur_elem.value, cur_elem.key
        distances[cur_node] = cur_dist
        for nbr in G.adj[cur_node]:
            new_dist = cur_dist + G.w(cur_node, nbr)
            if new_dist < distances[nbr] and relaxations[nbr] < k:
                pq.decrease_key(nbr, new_dist)
                distances[nbr] = new_dist
                relaxations[nbr] += 1

    return distances
