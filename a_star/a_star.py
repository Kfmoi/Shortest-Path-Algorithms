from given_code.final_project_part1 import DirectedWeightedGraph
from given_code.min_heap2 import MinHeap, Element


def a_star(G: DirectedWeightedGraph, s: int, d: int, h: dict[int, float]) -> tuple[dict[int, int], int]:
    g_distances = {}
    predecessors = {}
    f_scores = {}
    # Keep track of all the nodes in the priority queue. This is to make sure that nodes that were popped
    # previously from the heap but have gotten better scores from the heuristics are reconsidered
    in_pq = set()
    pq = MinHeap([])
    for node in G.adj.keys():
        g_distances[node] = float('inf')
        f_scores[node] = float('inf')
        pq.insert(Element(node, f_scores[node]))
        in_pq.add(node)

    g_distances[s] = 0
    f_scores[s] = g_distances[s] + h[s]
    pq.decrease_key(s, f_scores[s])
    while not pq.is_empty():
        cur_elem = pq.extract_min()
        cur_node, cur_score = cur_elem.value, cur_elem.key
        in_pq.remove(cur_node)
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
                if nbr in in_pq:
                    pq.decrease_key(nbr, f_scores[nbr])
                else:
                    pq.insert(Element(nbr, f_scores[nbr]))

    return predecessors, g_distances[d]
