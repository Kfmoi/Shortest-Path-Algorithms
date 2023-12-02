import random

import matplotlib.pyplot as plt


def create_plot(x_vals: list,
                y_vals: list[list],
                legend_labels: list[str],
                title: str,
                description: str,
                x_label: str,
                y_label: str,
                scale: float = 1,
                show_ticks: bool = True) -> None:
    height, width = plt.figure().get_figheight(), plt.figure().get_figwidth()
    plt.figure(figsize=(scale * width, scale * height))
    for yv, legend in zip(y_vals, legend_labels):
        plt.plot(x_vals, yv, linewidth=2, label=legend, marker='o')

    plt.xlabel(x_label)
    if show_ticks:
        plt.xticks(x_vals)
    plt.ylabel(y_label)
    plt.suptitle(title, fontsize=14)
    plt.title(description, fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
