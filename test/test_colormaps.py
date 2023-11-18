import unittest

import matplotlib.pyplot as plt
from cycler import cycler
from matplotlib.colors import ListedColormap

from aesthema import Colors
from aesthema.colormaps import Colormaps, create_colormap, use_colormap


class TestColormaps(unittest.TestCase):
    """Tests functionalities for colormaps."""

    def test_create_colormap(self):
        """Tests creating colormaps."""
        aesthema_colormap = create_colormap(
            [
                Colors.RED,
                Colors.ORANGE,
                Colors.YELLOW,
                Colors.PERSIAN_GREEN,
                Colors.VIVID_SKY_BLUE,
                Colors.BRIGHT_PINK_CRAYOLA,
            ]
        )
        self.assertTrue(isinstance(aesthema_colormap, ListedColormap))

        mixed_colormap = create_colormap(
            [
                Colors.RED,
                Colors.ORANGE,
                Colors.LEMON,
                (141, 215, 127),
                Colors.LIGHT_OCEAN,
                (47, 72, 88),
            ]
        )
        self.assertTrue(isinstance(mixed_colormap, ListedColormap))

        rgb_colormap = create_colormap(
            [
                (255, 0, 0),
                (255, 206, 0),
                (0, 252, 0),
                (0, 0, 255),
            ]
        )
        self.assertTrue(isinstance(rgb_colormap, ListedColormap))

    def test_use_colormap(self):
        """Tests setting colormaps."""
        self.assertEqual(
            plt.rcParams["axes.prop_cycle"],
            cycler(
                "color",
                [
                    "#1f77b4",
                    "#ff7f0e",
                    "#2ca02c",
                    "#d62728",
                    "#9467bd",
                    "#8c564b",
                    "#e377c2",
                    "#7f7f7f",
                    "#bcbd22",
                    "#17becf",
                ],
            ),
        )
        use_colormap()
        self.assertEqual(
            plt.rcParams["axes.prop_cycle"],
            cycler(
                "color",
                [
                    (
                        0.32941176470588235,
                        0.050980392156862744,
                        0.43137254901960786,
                        1.0,
                    ),
                    (0.9098039215686274, 0.2823529411764706, 0.3333333333333333, 1.0),
                    (1.0, 0.6078431372549019, 0.44313725490196076, 1.0),
                    (1.0, 0.8235294117647058, 0.24705882352941178, 1.0),
                    (0.23137254901960785, 0.807843137254902, 0.6745098039215687, 1.0),
                    (0.054901960784313725, 0.6784313725490196, 0.4117647058823529, 1.0),
                ],
            ),
        )

        use_colormap(cmap=Colormaps.HEAT)
        self.assertEqual(
            plt.rcParams["axes.prop_cycle"],
            cycler(
                "color",
                [
                    (0.5568627450980392, 0.5568627450980392, 0.5568627450980392, 1.0),
                    (0.6941176470588235, 0.6078431372549019, 0.6784313725490196, 1.0),
                    (0.8941176470588236, 0.6392156862745098, 0.6980392156862745, 1.0),
                    (1.0, 0.6941176470588235, 0.615686274509804, 1.0),
                    (1.0, 0.8117647058823529, 0.49411764705882355, 1.0),
                    (0.9764705882352941, 0.9725490196078431, 0.44313725490196076, 1.0),
                ],
            ),
        )


if __name__ == "__main__":
    unittest.main()
