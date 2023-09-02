"""Provides custom colormaps for Matplotlib."""
from enum import Enum
from typing import List, Optional, Tuple, Union

import matplotlib
from cycler import cycler

from .colors import Colors


def create_colormap(
    colors: List[Union[Colors, Tuple[int, int, int]]]
) -> matplotlib.colors.ListedColormap:
    used_colors = []
    for color in colors:
        if isinstance(color, Colors):
            used_colors.append(color.value)
        elif isinstance(color, tuple) and len(color) == 3:
            used_colors.append(color)
        else:
            raise ValueError(
                "Invalid color format when creating a new colormap. "
                "Use either a color from the Colors enum or a tuple containing RGB values."
            )
    return matplotlib.colors.ListedColormap(
        [tuple(color_value / 255 for color_value in color) for color in used_colors]
    )


class Colormaps(Enum):
    PASTEL = create_colormap(
        [
            Colors.TEA_GREEN,
            Colors.WHEAT,
            Colors.DESERT_SAND,
            Colors.OLD_ROSE,
            Colors.WENGE,
            Colors.CINEREOUS,
        ]
    )
    HEAT = create_colormap(
        [
            Colors.GRAY,
            Colors.HEATHER,
            Colors.INTENSE_ROSE,
            Colors.SALMON,
            Colors.OLD_ORANGE,
            Colors.LEMON,
        ]
    )
    RETRO = create_colormap(
        [
            Colors.LIGHT_BLACK,
            Colors.LIGHT_PETROL,
            Colors.LIGHT_TURQUOISE,
            Colors.LIGHT_OCEAN,
            Colors.IVORY,
            Colors.LIGHT_ORANGE,
            Colors.ORANGE,
            Colors.DARK_ORANGE,
            Colors.RED,
            Colors.BERRY,
        ]
    )


def use_colormap(
    cmap: Optional[Union[Colormaps, matplotlib.colors.ListedColormap]] = Colormaps.RETRO
) -> None:
    if isinstance(cmap, Colormaps):
        cmap = cmap.value
    matplotlib.pyplot.rcParams["axes.prop_cycle"] = cycler(
        color=[cmap(i) for i in range(cmap.N)]
    )
