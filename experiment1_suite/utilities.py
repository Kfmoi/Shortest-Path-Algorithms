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
                log_scale: bool = False,
                show_ticks: bool = True) -> None:
    height, width = plt.figure().get_figheight(), plt.figure().get_figwidth()
    plt.figure(figsize=(scale * width, scale * height))
    for yv, legend in zip(y_vals, legend_labels):
        plt.plot(x_vals, yv, linewidth=2, label=legend, marker='o')

    plt.xlabel(x_label)
    if show_ticks:
        plt.xticks(x_vals)
    if log_scale:
        plt.xscale('log')
        plt.yscale('log')
        plt.xlim(left=1, right=10e2)
        plt.ylim(bottom=10e-4,top=10e-1)

    plt.ylabel(y_label)
    plt.suptitle(title, fontsize=14)
    plt.title(description, fontsize=10)
    plt.legend(fontsize=10)
    plt.show()
