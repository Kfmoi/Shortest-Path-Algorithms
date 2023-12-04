from given_code.final_project_part1 import *
from approximations.dijkstra_approx import *
from approximations.bellman_ford_approx import *
from utilities import *

def experiment1():
        min_value = 1
        max_value = 50
        step = 1
        nodes = range(min_value,max_value + 1, step)
        k = 4
        reps = 100
        source = 0
        upper = 1000
        dijk_results = []
        bell_results = []

        for node in nodes:
            dijk_avg_distance = 0
            bell_avg_distance = 0
            for _ in range(reps):
                graph = create_random_complete_graph(node, upper)

                dijk_result = dijkstra_approx(graph, source, k)
                dijk_total = total_dist(dijk_result)
                dijk_avg_distance += dijk_total

                bell_result = bellman_ford_approx(graph, source, k)
                bell_total = total_dist(bell_result)
                bell_avg_distance += bell_total

            dijk_avg_distance /= reps
            bell_avg_distance /= reps

            dijk_results.append(dijk_avg_distance)
            bell_results.append(bell_avg_distance)

        create_plot(
            x_vals=nodes,
            y_vals=[dijk_results, bell_results],
            legend_labels=["Dijkstra", "Bellman-Ford"],
            title=f"Shortest Path Comparison of Dijkstra and Bellman-Ford Approximations with Varying Number of Nodes",
            description=f"{(max_value + 1 - min_value) // step} increments up to # of nodes = {max_value} from nodes = {min_value} with {reps} "
                        f"repetitions per increment, number of relaxations set to {k}, source node index = {0}, and max edge weights upto {upper}",
            x_label="Number of Nodes",
            y_label="Average Total Distance",
            scale=2,
            show_ticks=False
        )

if __name__ == '__main__':
    experiment1()
