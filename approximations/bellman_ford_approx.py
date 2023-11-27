from given_code.final_project_part1 import DirectedWeightedGraph


def bellman_ford_approx(G: DirectedWeightedGraph, source: int, k: int) -> dict[int, float]:
    distances = {}
    relaxations = {}
    for node in G.adj.keys():
        distances[node] = float('inf')
        relaxations[node] = 0

    distances[source] = 0
    # Might have k updates on someone after their predecessor updates to a lower point after a while
    for _ in range(G.number_of_nodes()):
        for node in G.adj.keys():
            for nbr in G.adj[node]:
                new_dist = distances[node] + G.w(node, nbr)
                if new_dist < distances[nbr] and relaxations[nbr] < k:
                    distances[nbr] = new_dist
                    relaxations[nbr] += 1

    return distances
