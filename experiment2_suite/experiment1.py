from timeit import default_timer as timer

from a_star.a_star import *
from given_code.min_heap2 import MinHeap, Element
from london_graph.station_graph import distance, create_london_subway_graph
from utilities import *


def p2p_dijkstra(graph: DirectedWeightedGraph, source, dest):
    pred = {}  # Predecessor dictionary. Isn't returned, but here for your understanding
    dist = {}  # Distance dictionary
    pq = MinHeap([])
    nodes = list(graph.adj.keys())

    # Initialize priority queue/heap and distances
    for node in nodes:
        pq.insert(Element(node, float("inf")))
        dist[node] = float("inf")
    pq.decrease_key(source, 0)

    # Meat of the algorithm
    while not pq.is_empty():
        current_element = pq.extract_min()
        current_node = current_element.value
        dist[current_node] = current_element.key
        if current_node == dest:
            break
        for neighbour in graph.adj[current_node]:
            if dist[current_node] + graph.w(current_node, neighbour) < dist[neighbour]:
                pq.decrease_key(neighbour, dist[current_node] + graph.w(current_node, neighbour))
                dist[neighbour] = dist[current_node] + graph.w(current_node, neighbour)
                pred[neighbour] = current_node

    return pred, dist[dest]



def base_experiment(graph: DirectedWeightedGraph, station_info, start_locations, end_locations, title_text):
    x_vals = [i + 1 for i in range(len(start_locations))]
    reps = 100
    a_star_times, dijkstra_times = [], []
    for source, dest in zip(start_locations, end_locations):
        heuristic = {}
        dest_lat, dest_long = station_info[dest]['latitude'], station_info[dest]['longitude']
        # A_star heuristic time excluded
        for node in graph.adj.keys():
            heuristic[node] = distance(station_info[node]['latitude'], station_info[node]['longitude'],
                                       dest_lat, dest_long)

        as_time, dj_time = 0, 0
        for _ in range(reps):
            start = timer()
            preds, dists = a_star(graph, source, dest, heuristic)
            end = timer()
            as_time += end - start
            start = timer()
            preds, dist = p2p_dijkstra(graph, source, dest)
            end = timer()
            dj_time += end - start

        a_star_times.append(as_time / reps)
        dijkstra_times.append(dj_time / reps)

    y_vals = [dijkstra_times, a_star_times]

    create_bar_plot(x_vals,
                    y_vals,
                    legend_labels=['Dijkstra', 'A*'],
                    title=f'{title_text} Stations Average Execution Times for A* and Dijkstra',
                    description=f'10 Station Pairs with {reps} Repetitions per Pairing',
                    x_label='Station Pairing',
                    y_label='Average Time (s)',
                    scale=1.25,
                    show_ticks=True)


def main():
    start_locations_a = [169, 169, 169, 279, 41, 6, 6, 11, 239, 193]
    end_locations_a = [12, 55, 157, 41, 253, 115, 271, 282, 296, 84]
    start_locations_b = [169, 169, 169, 279, 41, 6, 6, 11, 239, 193]
    end_locations_b = [193, 107, 57, 19, 289, 279, 197, 274, 11, 224]
    start_locations_c = [169, 60, 268, 88, 224, 165, 23, 5, 239, 267]
    end_locations_c = [6, 267, 60, 276, 88, 28, 88, 207, 5, 224]
    graph, station_info = create_london_subway_graph()
    base_experiment(graph, station_info, start_locations_a, end_locations_a, 'Same Line')
    base_experiment(graph, station_info, start_locations_b, end_locations_b, '1-Line Transfer')
    base_experiment(graph, station_info, start_locations_c, end_locations_c, 'Multiple Line Transfer')


if __name__ == '__main__':
    main()
