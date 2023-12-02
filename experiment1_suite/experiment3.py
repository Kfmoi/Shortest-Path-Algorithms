from given_code.final_project_part1 import *
from approximations.dijkstra_approx import *
from approximations.bellman_ford_approx import *
from utilities import *

def experiment3():
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
        dijk_avg_distance = 0
        bell_avg_distance = 0
        for _ in range(reps):
            graph = create_random_complete_graph(nodes, 1000)

            dijk_result = dijkstra_approx(graph, source, values)
            dijk_total = total_dist(dijk_result)
            dijk_avg_distance += dijk_total

            bell_result = bellman_ford_approx(graph, source, values)
            bell_total = total_dist(bell_result)
            bell_avg_distance += bell_total

        dijk_avg_distance /= reps
        bell_avg_distance /= reps

        dijk_results.append(dijk_avg_distance)
        bell_results.append(bell_avg_distance)

    create_plot(
        x_vals= k,
        y_vals=[dijk_results, bell_results],
        legend_labels=["Dijkstra", "Bellman-Ford"],
        title="Shortest Path Comparison of Dijkstra and Bellman-Ford Approximations with Varying Number of Relaxations",
        description=f"{(max_value + 1 - min_value) // step} increments up to # of relaxations = {max_value} from # of relaxations = {min_value} with {reps} "
                        f"repetitions per increment, number of nodes set to {nodes}, source node index = {0}, and max edge weights upto {upper}",
        x_label="Number of Relaxations",
        y_label="Average Total Distance",
        scale=1,
        show_ticks=False
    )
if __name__ == '__main__':
    experiment3()