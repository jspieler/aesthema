import numpy as np
import matplotlib.pyplot as plt

from aesthema import create_colormap, use_colormap, Colormaps, Colors


if __name__ == "__main__":
    use_colormap()
    # you can also use a different colormap or create your own:
    # my_colormap = create_colormap(
    #     [
    #         Colors.RED,
    #         Colors.ORANGE,
    #         Colors.LEMON,
    #         (141, 215, 127),
    #         Colors.LIGHT_OCEAN,
    #         (47, 72, 88),
    #     ]
    # )
    # use_colormap(my_colormap)

    x = np.linspace(0, 2 * np.pi, 100)

    plt.figure()

    plt.plot(x, np.sin(x))
    plt.plot(x, np.cos(x))
    plt.plot(x, np.sin(x + np.pi / 4))
    plt.plot(x, np.cos(x + np.pi / 4))
    plt.plot(x, np.sin(2 * x))
    plt.plot(x, np.cos(2 * x))

    plt.title("Sine and Cosine")
    plt.xlabel("x")
    plt.ylabel("Amplitude")
    plt.show()
