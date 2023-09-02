"""Provides custom colormaps for Matplotlib."""
from enum import Enum
from typing import List, Optional

import matplotlib
from cycler import cycler

from .colors import Colors


def create_colormap(colors: List[Colors]) -> matplotlib.colors.ListedColormap:
    return matplotlib.colors.ListedColormap(
        [tuple(color_value / 255 for color_value in color.value) for color in colors]
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


def use_colormap(cmap: Optional[Colormaps] = Colormaps.RETRO) -> None:
    matplotlib.pyplot.rcParams["axes.prop_cycle"] = cycler(
        color=[cmap.value(i) for i in range(cmap.value.N)]
    )
