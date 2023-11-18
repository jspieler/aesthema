"""Provides custom colormaps for Matplotlib."""
from enum import Enum
from typing import List, Optional, Tuple, Union

import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
from cycler import cycler

from .colors import Colors


def create_colormap(
    colors: List[Union[Colors, Tuple[int, int, int]]]
) -> ListedColormap:
    """Creates a Matplotlib ListedColormap given either colors from 
    the Colors enum or RGB values."""
    used_colors = []
    for color in colors:
        if isinstance(color, Colors):
            used_colors.append(color.value)
        elif isinstance(color, tuple) and len(color) == 3:
            used_colors.append(color)
        else:
            raise ValueError(
                "Invalid color format when creating a new colormap. "
                "Use either a color from the Colors enum or a tuple "
                "containing RGB values."
            )
    return ListedColormap(
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
    ASPECT = create_colormap(
        [
            Colors.CADET_GRAY,
            Colors.SILVER,
            Colors.MYRTLE_GREEN,
            Colors.CHINESE_VIOLET,
            Colors.REDWOOD,
            Colors.IMPERIAL_RED,
        ]
    )
    AUTUMN = create_colormap(
        [
            Colors.DARK_SLATE_GRAY,
            Colors.CARRIBEAN_CURRENT,
            Colors.CHAMPAGNE_PINK,
            Colors.PERSIAN_RED,
            Colors.BURNT_UMBER,
            Colors.OCHRE,
        ]
    )
    RETRO_SUMMER = create_colormap(
        [
            Colors.PERSIAN_GREEN,
            Colors.CARRIBEAN_CURRENT,
            Colors.SPACE_CADET,
            Colors.EBONY,
            Colors.MOSS_GREEN,
            Colors.ICTERINE,
            Colors.SUNSET,
            Colors.ATOMIC_TANGERINE,
            Colors.CRAYOLA,
        ]
    )
    LATE_SUMMER = create_colormap(
        [
            Colors.SAGE,
            Colors.VANILLA,
            Colors.PEACH_YELLOW,
            Colors.ATOMIC_TANGERINE,
            Colors.BITTERSWEET,
            Colors.REDWOOD,
            Colors.WINE,
            Colors.VAN_DYKE,
        ]
    )
    BLUE = create_colormap(
        [
            Colors.COLUMBIA_BLUE,
            Colors.OXFORD_BLUE,
            Colors.SAPPHIRE,
            Colors.BICE_BLUE,
            Colors.PRUSSIAN_BLUE,
        ]
    )
    SIMPLE = create_colormap(
        [
            Colors.XANTHOUS,
            Colors.LIGHT_SEA_GREEN,
            Colors.TAUPE_GRAY,
            Colors.BITTERSWEET,
            Colors.ASPARAGUS,
            Colors.MULBERRY,
        ]
    )
    BRIGHT = create_colormap(
        [
            Colors.HOLLYWOOD_CERISE,
            Colors.ELECTRIC_BLUE,
            Colors.SPRING_BUD,
            Colors.YELLOW,
            Colors.ORANGE_WHEEL,
            Colors.RED_CYMK,
        ]
    )
    SWEET = create_colormap(
        [
            Colors.BRIGHT_PINK_CRAYOLA,
            Colors.BABY_POWDER,
            Colors.CELESTE,
            Colors.CADET_GRAY,
            Colors.EGGPLANT,
            Colors.RAISIN_BLACK,
        ]
    )
    HIGH_CONTRAST = create_colormap(
        [
            Colors.INDIGO,
            Colors.CRAYOLA,
            Colors.ATOMIC_TANGERINE,
            Colors.SUNGLOW,
            Colors.TURQUOISE,
            Colors.JADE,
        ]
    )
    EARLY_SPRING = create_colormap(
        [
            Colors.POWDER_BLUE,
            Colors.LIGHT_BLUE,
            Colors.CREAM,
            Colors.WHEAT,
            Colors.APRICOT,
            Colors.TAN,
        ]
    )
    PALE_NIGHT = create_colormap(
        [
            Colors.POMP_AND_POWER,
            Colors.FRENCH_GRAY,
            Colors.CAMBRIDGE_BLUE,
            Colors.SAGE,
            Colors.HUNYADI_YELLOW,
            Colors.COCOA_BROWN,
            Colors.PERSIAN_RED,
        ]
    )


def use_colormap(
    cmap: Optional[Union[Colormaps, ListedColormap]] = Colormaps.HIGH_CONTRAST
) -> None:
    """Sets the colormap used for Matplotlib.

    Args:
        cmap: An Aesthema or Matplotlib colormap. Defaults to Colormaps.HIGH_CONTRAST.
    """
    if isinstance(cmap, Colormaps):
        cmap = cmap.value
    plt.rcParams["axes.prop_cycle"] = cycler(color=[cmap(i) for i in range(cmap.N)])
