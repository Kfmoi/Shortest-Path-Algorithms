from given_code.final_project_part1 import *
from utilities import *
import time


def mystery_loglog():
    num_nodes = range(0, 101, 1)
    reps = 50
    runtimes = []
    for node in num_nodes:
        avg_time = 0
        for _ in range(reps):
            G = create_random_complete_graph(node, 20)
            start = time.time()
            mystery(G)
            end = time.time()
            avg_time += end - start
        print(node)
        avg_time /= reps
        runtimes.append(avg_time)

    create_plot(
        x_vals=num_nodes,
        y_vals=[runtimes],
        legend_labels=["Mystery algorithm"],
        title="Mystery Algorithm Time-Complexity on Log-Log Scale",
        description=f" ",
        x_label=" Number of Nodes",
        y_label="Runtime(s)",
        scale=1,
        log_scale=True
    )


if __name__ == '__main__':
    mystery_loglog()
