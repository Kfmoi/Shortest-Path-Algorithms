from graph import Graph
import given_code.min_heap2 as min_heap
from given_code.min_heap2 import Element, MinHeap


class SPAlgorithm:
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pass


class Dijkstra(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
        dist = {}  # Distance dictionary
        Q = min_heap.MinHeap([])
        nodes = list(graph.adj.keys())

        # Initialize priority queue/heap and distances
        for node in nodes:
            Q.insert(min_heap.Element(node, float("inf")))
            dist[node] = float("inf")
        Q.decrease_key(source, 0)

        # Meat of the algorithm
        while not Q.is_empty():
            current_element = Q.extract_min()
            current_node = current_element.value
            dist[current_node] = current_element.key
            if current_node == dest:
                break
            for neighbour in graph.adj[current_node]:
                if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                    Q.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                    dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                    pred[neighbour] = current_node
        return dist[dest]


class Bellman_Ford(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        pred = {}  # Predecessor dictionary
        dist = {}  # Distance dictionary
        nodes = list(graph.adj.keys())

        # Initialize distances
        for node in nodes:
            dist[node] = float("inf")
        dist[source] = 0

        # Relax edges repeatedly
        for _ in range(graph.get_num_of_nodes()):
            for node in nodes:
                for neighbour in graph.adj[node]:
                    if dist[neighbour] > dist[node] + graph.w(node, neighbour):
                        dist[neighbour] = dist[node] + graph.w(node, neighbour)
                        pred[neighbour] = node
        return dist[dest]


class A_Star(SPAlgorithm):
    def calc_sp(self, graph: Graph, source: int, dest: int) -> float:
        def a_star(G, s, d, h):
            g_distances = {}
            predecessors = {}
            f_scores = {}
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

            return g_distances[d]

        heuristic = graph.get_heuristic()
        return a_star(graph, source, dest, heuristic)
