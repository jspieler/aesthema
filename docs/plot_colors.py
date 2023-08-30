"""Visualizes all available colors.

Based on https://matplotlib.org/stable/gallery/color/named_colors.html.
"""
import math
from enum import Enum

from matplotlib.figure import Figure
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle

from aesthema_colormaps import Colors


def plot_colors(colors: Colors, ncols: int = 4, sort_colors: bool = True) -> Figure:
    cell_width = 212
    cell_height = 22
    swatch_width = 48
    margin = 12

    # Sort colors by name, sorting by rgb values might follow
    if sort_colors:
        sorted_colors = sorted(
            [(color.name, color) for color in Colors], key=lambda x: x[0]
        )
        colors = Enum("Colors", [(name, color.value) for name, color in sorted_colors])

    n = len(colors)
    nrows = math.ceil(n / ncols)

    width = cell_width * 4 + 2 * margin
    height = cell_height * nrows + 2 * margin
    dpi = 72

    fig, ax = plt.subplots(figsize=(width / dpi, height / dpi), dpi=dpi)
    fig.subplots_adjust(
        margin / width,
        margin / height,
        (width - margin) / width,
        (height - margin) / height,
    )
    ax.set_xlim(0, cell_width * 4)
    ax.set_ylim(cell_height * (nrows - 0.5), -cell_height / 2.0)
    ax.yaxis.set_visible(False)
    ax.xaxis.set_visible(False)
    ax.set_axis_off()

    for i, color in enumerate(colors):
        row = i % nrows
        col = i // nrows
        y = row * cell_height

        swatch_start_x = cell_width * col
        text_pos_x = cell_width * col + swatch_width + 7

        ax.text(
            text_pos_x,
            y,
            color.name.replace("_", " ").title(),
            fontsize=14,
            horizontalalignment="left",
            verticalalignment="center",
        )

        ax.add_patch(
            Rectangle(
                xy=(swatch_start_x, y - 9),
                width=swatch_width,
                height=18,
                facecolor=[x / 255.0 for x in color.value],
                edgecolor="0.7",
            )
        )

    return fig


if __name__ == "__main__":
    fig = plot_colors(Colors)
    plt.show()
