from given_code.final_project_part1 import *
from approximations.dijkstra_approx import *
from approximations.bellman_ford_approx import *
from utilities import *

def experiment4():
    min_value = 1
    max_value = 16
    step = 1
    nodes = 20
    k = range(min_value,max_value,step)
    reps = 200
    source = 0
    upper = 1000
    dijk_results = []
    bell_results = []

    for values in k:
        dijk_matches = 0
        bell_matches = 0
        for _ in range(reps):
            graph = create_random_complete_graph(nodes, 1000)

            # calculate shortest path using Dijkstra
            actual_dijk_size = dijkstra(graph, source)
            actual_dijk_total = total_dist(actual_dijk_size)

            # calculate shortest path using Bellman-Ford
            actual_bell_size = bellman_ford(graph, source)
            actual_bell_total = total_dist(actual_bell_size)

            # calculate shortest path using Dijkstra approximation
            dijk_result = dijkstra_approx(graph, source, values)
            dijk_total = total_dist(dijk_result)

            # calculate shortest path using Bellman-Ford approximation
            bell_result = bellman_ford_approx(graph, source, values)
            bell_total = total_dist(bell_result)

            if actual_dijk_total == dijk_total:
                dijk_matches += 1
            if actual_bell_total == bell_total:
                bell_matches += 1

        approx_dijk_percent = (dijk_matches / reps) * 100
        approx_bell_percent = (bell_matches / reps) * 100

        dijk_results.append(approx_dijk_percent)
        bell_results.append(approx_bell_percent)

    create_plot(
        x_vals= k,
        y_vals=[dijk_results, bell_results],
        legend_labels=["Dijkstra", "Bellman-Ford"],
        title="Accuracy of Dijkstra and Bellman-Ford Approximations with Varying Number of Relaxations ",
        description=f"{(max_value + 1 - min_value) // step} increments up to # of relaxations = {max_value} from # of relaxations = {min_value} with {reps} "
                        f"repetitions per increment, number of nodes set to {nodes}, source node index = {0}, and max edge weights upto {upper}",
        x_label="Number of Relaxations",
        y_label="Accuracy of Approximation(%)",
        scale=1,
        show_ticks=False
    )
if __name__ == '__main__':
    experiment4()