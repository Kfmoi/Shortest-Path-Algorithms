from timeit import default_timer as timer

from a_star.a_star import *
from given_code.final_project_part1 import dijkstra
from london_graph.station_graph import distance, create_london_subway_graph
from utilities import *


def run_experiment(graph: DirectedWeightedGraph, station_info):
    x_vals = ['All Pairs']
    reps = 5
    a_star_times, dijkstra_times = [], []
    heuristics = {}
    for dest in graph.adj.keys():
        heuristics[dest] = {}
        dest_long = station_info[dest]['longitude']
        dest_lat = station_info[dest]['latitude']
        for node in graph.adj.keys():
            heuristics[dest][node] = distance(dest_lat, dest_long, station_info[node]['latitude'],
                                              station_info[node]['longitude'])

    as_time = 0
    for rep in range(reps):
        start_time = timer()
        # for every source
        for source in graph.adj.keys():
            # for every destination (source-dest) pairing
            for dest in graph.adj.keys():
                # skip if same destination as source
                if source == dest:
                    continue
                # calculate the heuristic
                # Calculate shortest path from source to dest
                _, __ = a_star(graph, source, dest, heuristics[dest])

        end_time = timer()
        as_time += end_time - start_time

    dj_time = 0
    for rep in range(reps):
        start_time = timer()
        # For every source, calculate Dijkstra's from that source
        for source in graph.adj.keys():
            _ = dijkstra(graph, source)
        end_time = timer()
        dj_time += end_time - start_time

    a_star_times.append(as_time / reps)
    dijkstra_times.append(dj_time / reps)

    y_vals = [dijkstra_times, a_star_times]

    create_bar_plot(x_vals,
                    y_vals,
                    legend_labels=['Dijkstra', 'A*'],
                    title=f'All Pairs Shortest Paths Average Execution Times for A* and Dijkstra',
                    description=f'All Station Pairs with {reps} Repetitions per Algorithm',
                    x_label='All Pairs Shortest Paths',
                    y_label='Average Time (s)',
                    scale=1.25,
                    show_ticks=True,
                    bar_width=1)


def main():
    graph, station_info = create_london_subway_graph()
    run_experiment(graph, station_info)


if __name__ == '__main__':
    main()
