"""Visualizes all available colormaps."""
import math
from enum import Enum

from matplotlib.figure import Figure
import matplotlib.pyplot as plt

from aesthema import Colormaps


def plot_colormaps(
    colormaps: Colormaps, ncols: int = 4, sort_colors: bool = True
) -> Figure:
    cell_width = 212
    cell_height = 22
    swatch_width = 100
    margin = 12
    ncols = 2

    if sort_colors:
        sorted_colormaps = sorted(
            [(colormap.name, colormap) for colormap in Colormaps], key=lambda x: x[0]
        )
        colormaps = Enum(
            "Colormaps", [(name, colormap.value) for name, colormap in sorted_colormaps]
        )

    n = len(colormaps)
    nrows = math.ceil(n / ncols)

    width = cell_width * ncols + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - margin) / height,
    )
    ax.set_xlim(0, cell_width * ncols)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, colormap in enumerate(colormaps):
        num_colors = colormap.value.N
        rect_width = 10
        rect_height = 10

        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(
            text_pos_x,
            y + rect_height / 2,
            colormap.name.replace("_", " ").title(),
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )

        for i in range(num_colors):
            color = colormap.value(i)
            ax.add_patch(
                plt.Rectangle(
                    (swatch_start_x + i * rect_width, y),
                    rect_width,
                    rect_height,
                    color=color,
                )
            )

    return fig


if __name__ == "__main__":
    fig = plot_colormaps(Colormaps)
    plt.show()
